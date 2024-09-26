import random

def GuessNumber0to9():
    com_n = random.randint(0,9)

    print("~=~=~=~=~=~=~> Welcome to 'Guess the Number' game...! <~=~=~=~=~=~=~")
    print("==> I have chosen a number between 0 and 9. You have 5 rounds to guess it.")

    for i in range(1, 6):
        my_n = int(input(f"=> Round {i} : Enter your Guess Number : "))

        if my_n == 'exit':
            print("\n===> You Have QUIT the game...! ")
            guess_game()

        else:
            if com_n == my_n:
                print(f"~~~> Congratulations! You've guessed the number correctly! It was {com_n}.")
                break
            else:
                if i < 5:
                    print("---> Wrong guess, try again!")
                else:
                    print(f"---> Sorry, you've used all your rounds. The correct number was {com_n}.")
            
GuessNumber0to9()