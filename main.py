# imports
import random
from colorama import Fore, Back, Style
from backup import alot_2
from time import sleep
from alive_progress import alive_bar, config_handler
import os


# global variables
config_handler.set_global(length=50, spinner="dots")
player_global = 0
dealer_global = 0
games_drawn = 0
printgames = True


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
    print("\033c", end="")  # ANSI escape code to clear the screen


# basic functions (for the next 2 functions)
def info():
    print(Fore.LIGHTBLACK_EX + "")
    print(
        "   The system will get two cards for the player, then compare the players cards to the dealers to determine who won. The main function, playblackjack() runs one game with a report. The other function, alot(x) runs x games without a game by game report.Also ensure the kernal has a decent amount of space horizontally in order for the alot(x) to work as intended, lastly the many(x) function is alot(x) but faster and w/o a neat animation bar"
    )
    reset()


def reset():  # recallable for resetting the font of the prints
    print(Style.RESET_ALL)


# our basic blackjack function
def blackjack():
    clear_console()
    print("")
    global player_global
    global dealer_global
    global games_drawn
    global printgames
    player = 0
    dealer = random.randint(1, 100)  # percent assignment for the dealer
    cards = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
    ]
    for i in range(2):  # give the player 2 cards
        x = random.randint(0, 51)
        carddrawn = cards[x]
        player += carddrawn
        del cards[x]
    if dealer >= 1 and dealer <= 10:  # starts to determine the dealers score
        dealer = 16
    if dealer >= 11 and dealer <= 25:
        dealer = 17
    if dealer >= 21 and dealer <= 35:
        dealer = 18
    if dealer >= 31 and dealer <= 50:
        dealer = 19
    if dealer >= 51 and dealer <= 65:
        dealer = 20
    if dealer >= 66 and dealer <= 75:
        dealer = 21
    if dealer >= 76 and dealer <= 100:
        dealer = "BUST"
    if player > 21:
        player = "BUST"
    if printgames == True:  # if you used this function to run then return game results
        print(Fore.GREEN + "Player score", player)
        reset()
        print(Fore.YELLOW + "Dealer score", dealer)
        reset()
        if player == dealer:
            games_drawn += 1
            print(Fore.CYAN + "Game is drawn")
            reset()
        elif dealer == "BUST":
            player_global += 1
            print(Fore.GREEN + "Dealer is bust!")
            reset()
        elif player == "BUST":
            dealer_global += 1
            print(Fore.RED + "Player is bust!")
            reset()
        elif player != "BUST" and dealer != "BUST":
            if player > dealer:
                player_global += 1
                print(Fore.GREEN + "Player is closer to 21!")
                reset()
            elif player < dealer:
                dealer_global += 1
                print(Fore.RED + "Dealer is closer to 21!")
                reset()
    elif printgames == False:  # if you used the alot function do not print game results
        if player == dealer:
            games_drawn += 1
        elif dealer == "BUST":
            player_global += 1
        elif player == "BUST":
            dealer_global += 1
        elif player != "BUST" and dealer != "BUST":
            if player > dealer:
                player_global += 1
            elif player < dealer:
                dealer_global += 1
    else:  # if an error dont break entirely
        print(Back.RED + "")
        print("ERROR")
        reset()


# play just one blackjack game that allows the alot function to work as intended
def playblackjack():
    global printgames
    printgames = True
    blackjack()


# simulates many blackjacks
def alot(x):
    global player_global
    global dealer_global
    global games_drawn
    global printgames
    player_global = 0
    dealer_global = 0
    games_drawn = 0
    printgames = False
    items = range(x)
    with alive_bar(
        len(items), bar="smooth", calibrate=100
    ) as bar:  # imports code that I cannot explain
        for item in items:
            blackjack()  # plays one game of blackjack
            bar()  # updates the bar
            sleep(0.019)
        clear_console()
    print(Style.BRIGHT + "")  # starts to print games result totals
    print(Fore.GREEN + " • Player won", player_global, " games")
    print(Fore.YELLOW + " • Dealer won ", dealer_global, " games")
    print(Fore.CYAN + " • There were ", games_drawn, " games drawn")
    reset()


# the backup simulation function
def many(x):
    """This funciton only works with a quantity greater than or equal to 100"""
    alot_2(x)


def clown():
    print(" 🤡 ", end="")


def clowntime(z):
    for i in range(z):
        clown()


def main():
    print("Welcome to the blackjack simulator")
    print("1. Play blackjack")
    print("2. Simulate many blackjacks")
    print("3. Simulate many blackjacks (faster)")
    print("4. Clown time")
    print("5. Info")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        playblackjack()
    elif choice == "2":
        x = int(input("Enter the amount of games to simulate: "))
        alot(x)
    elif choice == "3":
        x = int(input("Enter the amount of games to simulate: "))
        many(x)
    elif choice == "4":
        z = int(input("Enter the amount of clowns: "))
        clowntime(z)
    elif choice == "5":
        info()
    elif choice == "6":
        exit()
    else:
        print("Invalid choice")
    input("Press enter to continue")
    clear_console()
    main()


if __name__ == "__main__":
    main()
