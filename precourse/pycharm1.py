import random

modes = ["rock", "paper", "scissors"]


def comp_turn():
    """The choice made by the computer"""
    comp = random.choice(modes)
    return comp


def calc_win(comp, move):
    """Determining the winner"""
    print("The computer chose {0}.".format(comp))
    win = None
    tie = False

    if move == comp:
        print("No winner.... Restarting....\n")
        main()
        tie = True
    elif ((comp == "rock") and (move == "paper")) or \
            ((comp == "paper") and (move == "scissors")) or \
            ((comp == "scissors") and (move == "rock")):
        win = True
    else:
        win = False

    return win, tie


def player_turn():
    """The choice made by the user"""
    move = ""
    while move not in modes:
        move = input("Choose your move (rock, paper, or scissors: ").lower()
    return move


def print_winner(win, tie):
    """Display the winner of the game."""
    if tie == True:
        print("")
    elif win == True:
        print("You beat the computer!")
    elif win == False:
        print("The computer beat you!")


def main():
    """This is the main function"""
    comp = comp_turn()
    move = player_turn()

    win, tie = calc_win(comp, move)
    print_winner(win, tie)


main()
