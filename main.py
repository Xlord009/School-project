import random
import tkinter as tk
import time
from getpass import getpass
from colorama import Fore



class stat:
    def __init__(self):
        self.token = 100
        self.emotional_state = 60
        self.aura = 0

my_stat = stat()


# Roulette spin
def spin():
    roulette = [
    (0, "green"), (1, "red"), (2, "black"), (3, "red"), (4, "black"), (5, "red"),
    (6, "black"), (7, "red"), (8, "black"), (9, "red"), (10, "black"), (11, "black"),
    (12, "red"), (13, "black"), (14, "red"), (15, "black"), (16, "red"), (17, "black"),
    (18, "red"), (19, "red"), (20, "black"), (21, "red"), (22, "black"), (23, "red"),
    (24, "black"), (25, "red"), (26, "black"), (27, "red"), (28, "black"), (29, "black"),
    (30, "red"), (31, "black"), (32, "red"), (33, "black"), (34, "red"), (35, "black"),
    (36, "red")
]
    number = roulette[0]
    color_choice = roulette[1]
    
    users_choice = input("would you prefer choosing a color or a number?(color)(number): ")
    bet_roullete = int(input("how many tokens are you betting?: "))
    if my_stat.token >= bet_roullete:
        my_stat.token - bet_roullete
        print(Fore.RED + f"-{bet_roullete}")
        if users_choice.lower() == "color":
            print("If you choose the right color you win 2x your bet")
            time.sleep(1)
            color_choice = input("Red or Black? or green(1/36): ")
            time.sleep(1)
            print("The ball has been dropped in the spinning roulette")
            time.sleep(0.5)
            random_ball_color = random.choice(roulette[1])
            print(f"The ball has landed on {random_ball_color}")
            if random_ball_color == color_choice:
                tokens_won = bet_roullete * 2
                my_stat.token + tokens_won
                print(f"You have won {tokens_won}!")
                print(Fore.GREEN + f"{tokens_won} has been added to your wallet!")
            else:
                print(Fore.RED + f"too bad, you didnt win anything, {bet_roullete} has been lost :(")
        elif users_choice.lower() == "number":
            number_choice = input("")           
             
    else:
        print("You do not have enough tokens!")
        time.sleep(1)
        print("Your getting kicked out of the casion you goy")
        tk.quit()


def blackjack():
    # create a list of all cards
    cards = [
    "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♠",
    "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", "A♥",
    "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦", "A♦",
    "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♣"
]

    token_in_game_blackjack = float(input("How much are you betting?: "))
    if token_in_game_blackjack <= my_stat.token and my_stat.emotional_state >= 10:
        print(f"You have betted {token_in_game_blackjack} tokens")
        time.sleep(1)
        print(Fore.RED + f"-{token_in_game_blackjack}")
        my_stat.token - token_in_game_blackjack
        time.sleep(1)
        # dealers deck generation
        dealers_deck1 = random.choice(cards)
        dealers_deck2 = random.choice(cards)
        # players deck generation
        players_deck1 = random.choice(cards)
        players_deck2 = random.choice(cards)
        print(f"Your cards {players_deck1} and {players_deck2}")
        #asks the user 
        change_cards = input("would you like to hit or stand?: ")
        if change_cards.lower() == "hit":
            time.sleep(0.5)
            change_1_2 = input("would you like to change the first card or the second card?: ")
            if change_1_2.lower() == "first" or change_1_2.lower() == "1":
                time.sleep(0.5)
                players_deck1 = random.choice(cards)
                print(Fore.RED + f"removed the first card and repleaced it with {players_deck1}")
            elif change_1_2.lower() == "second" or change_1_2.lower() == "2":
                time.sleep(0.5)
                players_deck2 = random.choice(cards)
                print(Fore.RED + f"removed the second card and repleaced it with {players_deck1}")
        elif change_cards.lower() == "stand":
            time.sleep(0.5)
            adding_up_cards = players_deck1 + players_deck2
            print(f"are you happy with {adding_up_cards}?")
            if adding_up_cards > 21:
                print("are you aware that you busted?")
            happy_choice_bl = input("are you happy with your deck?: ")
            time.sleep(0.5)
            if happy_choice_bl.lower() == "yes":
                adding_up_cards = players_deck1 + players_deck2
                





    elif token_in_game_blackjack > my_stat.token:
        print("you dont have enough tokens to place that bet")
        
        


# Password entry and display authorization
def pass_open():
    password = getpass("What is the password?: ")
    if password == "ADAM":
        print("Correct password, Welcome!")
        print("you have started your casino simulation life with 100 tokens")
        time.sleep(1)
        root1 = tk.Tk()
        root1.title("Gamble time")
        root1.minsize(400, 500)
        root1.geometry("300x300")
        root1.config(background= "purple")
        
        
        label_1 = tk.Label(root1, background="red", text= "Welcome to the casino!")
        label_1.pack()
        label_2 = tk.Label(root1, background="red", text="Where all of your money will be lost!")
        label_2.pack()
        spin_wheel = tk.Button(root1, background="red", text="Spin the wheel!", command=spin)
        spin_wheel.pack()

        blackack_button = tk.Button(root1, background="red", text="BlackJack!", command=blackjack)
        blackack_button.pack()
        
        
        root1.mainloop()
        
    else:
        print("wrong password")
        time.sleep(2)
        tk.quit

pass_open()
