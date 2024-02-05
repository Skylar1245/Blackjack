"""
THIS IS OUR BACKUP FILE. BECAUSE WE DON'T KNOW WHAT WE ARE DOING WE MADE THIS TO ENSURE THAT WE GET THE GRADE
"""

# imports
import random
from colorama import Fore, Back, Style

# initialize global variables
player_global = 0
dealer_global = 0
games_drawn = 0


# function to give information on how the game works
def info():
    print(Fore.LIGHTBLACK_EX + "")
    print(
        Back.WHITE
        + "   The system will get two cards for the player, then compare the   players cards to the deals to determine who won. The main function, blackjack() runs one game. The other function, alot(x) runs x games."
    )
    reset()


# function to reset font and text color
def reset():
    print(Style.RESET_ALL)


# the actual blackjack code
def blackjack_2():
    global player_global  # declare the global variables
    global dealer_global
    global games_drawn
    player = 0  # initialize
    dealer = random.randint(1, 100)
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
    ]  # make the deck of cards
    for i in range(2):  # draw the player's cards
        x = random.randint(0, 51)
        carddrawn = cards[x]
        player += carddrawn
        del cards[x]
    if (
        dealer >= 1 and dealer <= 10
    ):  # for the next 7 ifs; generating the dealer's numbers
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
    if player > 21:  # see if the player is bust
        player = "BUST"
    if player == dealer:  # if both are bust or they have the same number
        games_drawn += 1
    elif dealer == "BUST":  # next 9 lines; outcomes for a non-tied game
        player_global += 1
    elif player == "BUST":
        dealer_global += 1
    elif player != "BUST" and dealer != "BUST":
        if player > dealer:
            player_global += 1
        if player < dealer:
            dealer_global += 1


# function to simulate the blackjack many times
def alot_2(x):
    global player_global  # declare global variables
    global dealer_global
    global games_drawn
    player_global = 0  # initialize global variables
    dealer_global = 0
    games_drawn = 0
    for a in range(100):  # each loop simulates 1% of the total. So we do it 100 times
        for i in range(int(x / 100)):
            blackjack_2()
        print(a + 1, "% done.", sep="")  # report what % the program has simulated
    print(Style.BRIGHT + "")  # next 5 lines; to print games result totals
    print(Fore.GREEN + " • Player won", player_global, " games")
    print(Fore.YELLOW + " • Dealer won ", dealer_global, " games")
    print(Fore.CYAN + " • There were ", games_drawn, " games drawn")
    reset()
