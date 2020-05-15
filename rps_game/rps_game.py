dict_rps = {"Rock": 0, "Paper": 1, "Scissors": 2}
user_hand = int(input("Please enter a number between 0-2: "))

import random

computer_hand = random.randrange(0, 3)
print(computer_hand)


def get_hand(number):
    for rps, index in dict_rps.items():
        if number == index:
            dict_rps[rps] = index
            print(rps)
    return number


get_hand(user_hand)
get_hand(computer_hand)

computer_player = False
user_player = True

def determine_winner(hand):



# determine_winner(computer_hand, user_hand)
# * print out the player hand and computer hand
# * print out the winner
#
# ## Some Tips
#
# Creating a function that gets a "hand" based on a number.
#
# The function should take in a number and return the string representation of the hand. E.g.:
#