count = 0
while count == 0:
    dict_rps = {"Rock": 0, "Paper": 1, "Scissors": 2}
    user_hand = int(input("Please enter a number between 0-2: "))

    import random

    computer_hand = random.randrange(0, 3)


    def get_hand(number):
        for rps, index in dict_rps.items():
            if number == index:
                dict_rps[rps] = index
                print(rps)
        return number


    print("Your hand is: ", end='')
    get_hand(user_hand)
    print("Computer's hand is: ", end='')
    get_hand(computer_hand)

    score = computer_hand - user_hand


    def determine_winner(result):
        if score == 0:
            print("It is a Draw \n")
        elif score == (1, -2):
            print("You Win \n")
        else:
            print("The computer wins \n")
        return result


    determine_winner(score)
