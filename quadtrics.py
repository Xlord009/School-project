import math
import time
a = 0

def delta_pos():
    v1 = -b - math.sqrt(delta) / 2 * a
    v2 = -b + math.sqrt(delta) / 2 * a
    print(f"V1 = {v1} et V2 = {v2}")

def delta_neg():
    print("Delta doesnt a have unique solution")
    
def delta_equal():
    root3 = (-b / (2 * a))
    print(root3)

undefined_x = input("do you have an undefined x in the equation?: ")
if undefined_x.lower() == "yes" or undefined_x.lower() == "yeah":
    a_b_c_undefined_X = input("is it: a b or c who has the missing value?: ")
    if a_b_c_undefined_X == "a":
        a = 1
        time.sleep(1)
    elif a_b_c_undefined_X == "b":
        b = 1
        time.sleep(1)
    elif a_b_c_undefined_X == "c":
        c = 1
        time.sleep(1)
else:
    print("ok")
    time.sleep(1)
    pass
    

a = float(input("what is A square in the equation?: "))
b = float(input("what does b represent in the equation?: "))
c = float(input("what does c represent in the equation?: "))



if a == 0:
    if b == 0:
        if c == 0:
            print("The equation is degenerate. It has infinite solution..")
        else:
            print("The equation is degenerate. It has no solutions.")
    else:
        root = -c/b
        print(f"The equation is linear. It has no real root: x = {root}")

if a == "x":
    float(a) == 1

delta = (b ** 2) - (4 * a * c)


if delta > 0:
    delta_pos()

elif delta == 0:
    delta_equal() 


else:
    delta_neg()