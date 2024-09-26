import random

def guess_game():
    com_n = random.randint(1, 100)

    print("Welcome to 'Guess the Number' game!")
    print("I have chosen a number between 1 and 100. You have 10 rounds to guess it.")


    for i in range(1, 11):
        my_n = int(input(f"\nRound {i} : Enter your Guess Number : "))

        if my_n == com_n:
            print(f"\nCongratulations! You've guessed the number correctly! It was {com_n}.")
            break

        elif i == 10:
            print(f"\nSorry, you've used all your rounds. The correct number was {com_n}.")

        elif my_n < com_n:
            print("Your guess is LOW.")

        else:
            print("Your guess is HiGH.")

def GuessNumber0to100():
    com_n = random.randint(1, 20)

    print("\n~=~=~=~=~=~=~> Welcome to 'Guess the Number' game...! <~=~=~=~=~=~=~")
    print("==> I have chosen a number between 1 and 100. You have 10 rounds to guess it.")

    print("\n===> Welcome to 'Guess the Number' game!\n==> Type 'start' when you are ready and hit the 'Enter' key")
    player_input = input('=> Are you Ready For Game: ')

    while player_input != 'start':
        print("\n==> Type 'start' when you are ready nd hit the 'Enter' key")
        player_input = input('=> Are you Ready For Game: ')

    print("\n==> I have chosen a number between 1 and 100. You have 10 rounds to guess it.")

    for i in range(1, 11):
        my_n = input(f"\n=> Round {i} : Enter your Guess Number : ")

        if my_n == 'exit':
            print("\n===> You Have QUIT the game...! ")
            GuessNumber0to100()
        
        else:
            my_n = int(my_n)
            if my_n == com_n:
                print(f"\n~~~> Congratulations! You've guessed the number correctly! It was {com_n}.")
                break

            elif i == 10:
                print(f"\n---> Sorry, you've used all your rounds. The correct number was {com_n}.")

            elif my_n < com_n:
                print("=> Your guess is LOW.")

            else:
                print("=> Your guess is HiGH.")

GuessNumber0to100()