
import socket
import subprocess
import tempfile
import os
import time
from urllib.parse import quote

from zeroconf import Zeroconf, ServiceBrowser

SERVICE_TYPES = [
    "_ipp._tcp.local.",
    "_ipps._tcp.local.",
    "_printer._tcp.local.",
    "_pdl-datastream._tcp.local.",
]

discovered = {}


class PrinterListener:
    def add_service(self, zc, service_type, name):
        info = zc.get_service_info(service_type, name, timeout=5000)
        if not info:
            return

        addresses = [
            socket.inet_ntoa(addr)
            for addr in info.addresses
            if len(addr) == 4
        ]

        props = {
            k.decode("utf-8", errors="replace"):
            v.decode("utf-8", errors="replace")
            if isinstance(v, bytes) else str(v)
            for k, v in (info.properties or {}).items()
        }

        key = (name, tuple(addresses))
        entry = discovered.setdefault(key, {
            "name": name,
            "addresses": addresses,
            "model": props.get("ty") or props.get("product")
                     or props.get("model") or "Unknown",
            "services": {},
        })

        entry["services"][service_type] = {
            "port": info.port,
            "properties": props,
        }

    def update_service(self, zc, service_type, name):
        self.add_service(zc, service_type, name)

    def remove_service(self, zc, service_type, name):
        for key in list(discovered):
            if key[0] == name:
                del discovered[key]


def discover_printers():
    zc = Zeroconf()
    browsers = []

    try:
        listener = PrinterListener()
        browsers = [
            ServiceBrowser(zc, service, listener)
            for service in SERVICE_TYPES
        ]

        print("Discovering printers for 5 seconds...")
        time.sleep(5)
    finally:
        zc.close()

    # Group services by IP so each printer appears once.
    printers = {}

    for entry in discovered.values():
        for ip in entry["addresses"]:
            if ip not in printers:
                printers[ip] = {
                    "ip": ip,
                    "name": entry["name"],
                    "model": entry["model"],
                    "services": {},
                }
            printers[ip]["services"].update(entry["services"])

    return list(printers.values())


def configured_queues():
    result = subprocess.run(
        ["lpstat", "-p"],
        capture_output=True,
        text=True,
    )
    queues = []

    for line in result.stdout.splitlines():
        parts = line.split()
        if len(parts) >= 2 and parts[0] == "printer":
            queues.append(parts[1])

    return queues


def add_printer_queue(printer, protocol):
    ip = printer["ip"]
    queue = "network_printer_" + ip.replace(".", "_")

    # Use an explicitly advertised protocol.
    if protocol == "ipps":
        uri = f"ipps://{ip}:631/ipp/print"
    elif protocol == "ipp":
        uri = f"ipp://{ip}:631/ipp/print"
    elif protocol == "jetdirect":
        uri = f"socket://{ip}:9100"
    elif protocol == "lpd":
        uri = f"lpd://{ip}/queue"
    else:
        raise ValueError("Unsupported protocol.")

    print(f"\nThis will configure queue '{queue}' for {ip}.")
    print("It may require your macOS administrator password.")

    confirm = input("Continue? (yes/no): ").strip().lower()
    if confirm != "yes":
        return None

    # Generic PostScript is not supported by every printer.
    # Use a driverless IPP queue where supported.
    if protocol in ("ipp", "ipps"):
        command = [
            "lpadmin", "-p", queue,
            "-E",
            "-v", uri,
            "-m", "everywhere",
        ]
    else:
        print(
            "For this protocol, add the printer in "
            "System Settings > Printers & Scanners first, "
            "or configure a compatible driver."
        )
        return None

    result = subprocess.run(command, text=True, capture_output=True)

    if result.returncode != 0:
        print("Could not configure queue:")
        print(result.stderr.strip())
        print(
            "Try adding the printer through System Settings, "
            "or verify its supported IPP URL."
        )
        return None

    return queue


def print_message(queue, model):
    message = input("\nMessage to print: ")
    if not message.strip():
        print("Empty message; cancelled.")
        return

    print(f"\nPrinter: {queue}")
    print(f"Model: {model}")
    print(f"Message: {message}")

    if input("Submit this print job? (yes/no): ").strip().lower() != "yes":
        print("Cancelled.")
        return

    fd, path = tempfile.mkstemp(suffix=".txt", text=True)

    try:
        with os.fdopen(fd, "w", encoding="utf-8") as file:
            file.write(message + "\n")

        subprocess.run(["lp", "-d", queue, path], check=True)
        print("Print job submitted.")
    except (subprocess.CalledProcessError, OSError) as error:
        print(f"Printing failed: {error}")
    finally:
        if os.path.exists(path):
            os.unlink(path)


def main():
    printers = discover_printers()
    queues = configured_queues()

    if not printers:
        print("No network printers discovered.")
        return

    print("\nDiscovered printers:")
    for i, printer in enumerate(printers, 1):
        protocols = []
        services = printer["services"]

        if "_ipps._tcp.local." in services:
            protocols.append("IPPS")
        if "_ipp._tcp.local." in services:
            protocols.append("IPP")
        if "_pdl-datastream._tcp.local." in services:
            protocols.append("JetDirect")
        if "_printer._tcp.local." in services:
            protocols.append("LPD")

        print(f"\n{i}. {printer['name']}")
        print(f"   Model: {printer['model']}")
        print(f"   IP: {printer['ip']}")
        print(f"   Protocols: {', '.join(protocols) or 'Unknown'}")

    choice = input("\nChoose a printer number (or Enter to exit): ").strip()
    if not choice:
        return

    try:
        printer = printers[int(choice) - 1]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    print("\nAvailable connection methods:")
    protocols = printer["services"]

    options = []
    if "_ipps._tcp.local." in protocols:
        options.append(("ipps", "IPPS (encrypted IPP)"))
    if "_ipp._tcp.local." in protocols:
        options.append(("ipp", "IPP"))
    if "_pdl-datastream._tcp.local." in protocols:
        options.append(("jetdirect", "JetDirect"))
    if "_printer._tcp.local." in protocols:
        options.append(("lpd", "LPD"))

    for i, (_, label) in enumerate(options, 1):
        print(f"{i}. {label}")

    method = input("Choose a method: ").strip()
    try:
        protocol = options[int(method) - 1][0]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    # Prefer an existing queue if one matches the selected printer.
    queue = next(
        (q for q in queues if printer["ip"].replace(".", "_") in q),
        None,
    )

    if not queue:
        queue = add_printer_queue(printer, protocol)

    if not queue:
        print(
            "Printer queue not configured. Add it through "
            "System Settings > Printers & Scanners and try again."
        )
        return

    print_message(queue, printer["model"])


if __name__ == "__main__":
    main()
5