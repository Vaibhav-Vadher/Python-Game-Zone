import random

def RockPaperScissor():

    c = ['r', 'p', 's']

    my_score = 0
    com_score = 0

    while True:
        
        print("\n\n~=~=~=~=~=~=~> Welcome to Rock Paper Scissors Game...! <~=~=~=~=~=~=~\nPlease Enter R/r for Rock, P/p for Paper and S/s for Scissor")

        my_c = input("\nYour Turn : ").lower()

        if my_c == 'exit':
            print("\nYou Have Exit the Game...")
            RockPaperScissor()
        
        else:
            if my_c not in c:
                print("\nInvalid Input...!\nEnter R/r for Rock, P/p for Paper and S/s for Scissor")
                continue
                
            com_c = random.choice(c)
            print(f"Computer Choses : {com_c}")

            if my_c == com_c:
                print("\n===> Its a TIE <===")
            
            elif my_c == 'r' and com_c == 's' or my_c == 'p' and com_c == 'r' or my_c == 's' and com_c == 'p':
                print("\n===> You WON <===")
                my_score += 1
            
            else:
                print("\n===> You Loss <===")
                com_score += 1

        print(f"\nYour Score = {my_score} and Computer Score = {com_score}")

        if my_score == 10:
            print("\n~~~> Congratulations! You've won the game! <~~~")
        elif com_score == 10:
            print("\n---> Sorry, the computer has won the game! <---")

RockPaperScissor()