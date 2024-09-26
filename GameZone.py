import random

#GuessNumber0to9
def GuessNumber0to9():
    com_n = random.randint(0,9)

    print("~=~=~=~=~=~=~> Welcome to 'Guess the Number' game...! <~=~=~=~=~=~=~")
    print("==> I have chosen a number between 0 and 9. You have 5 rounds to guess it.")

    for i in range(1, 6):
        my_n = int(input(f"=> Round {i} : Enter your Guess Number : "))

        if my_n == 'exit':
            print("\n===> You Have QUIT the game...! ")
            GuessNumber0to9()

        else:
            if com_n == my_n:
                print(f"~~~> Congratulations! You've guessed the number correctly! It was {com_n}.")
                break
            else:
                if i < 5:
                    print("---> Wrong guess, try again!")
                else:
                    print(f"---> Sorry, you've used all your rounds. The correct number was {com_n}.")

#GuessNumber0to100
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

#HandCricket
def toss():
    print("\n=> Let's do the TOSS...!")
    toss_c = input("=> Choose 'heads' or 'tails' : ").lower()
    if toss_c == "exit":
        return "exit"
    
    toss_r = random.choice(['heads', 'tails'])

    if toss_c == toss_r:
        print("\n~~~> You WON the TOSS...! <~~~")
        play_c = input("\n=> Do you want to batting('bat') or bowling('bowl') first : ").lower()
        if play_c== "exit":
            return "exit"
    
    else:
        print("\n---> Computer WON the TOSS...! <---")
        play_c = random.choice(['heads', 'tails'])
        print(f"==> Computer chooses to {play_c} first.")

    return play_c

def player_batting():
    score = 0

    while True:
        play_r = int(input("\n=> Enter a number between 1 & 6 : "))
        if play_r == "exit":
            return "exit"

        if play_r < 1 or play_r > 6:
            print("\n==> Invalid Input...! Please enter a number between 1 & 6.")
            continue

        com_r = random.randint(1, 6)
        print(f"=> Computer Chooses : {com_r}")


        if play_r == com_r:
            print("\n---> OUT...! <---")
            break
        else:
            score += play_r
            print(f"===> Your Current Score : {score}. <===")

    return score

def computer_batting(traget = None):
    score = 0

    while True:
        com_r = random.randint(1, 6)
        print("\n==> Computer Chosen...! Your Turn.")

        play_r = int(input("=> Enter a number between 1 & 6 : "))
        if play_r == "exit":
            return "exit"

        if play_r < 1 or play_r > 6:
            print("\n==> Invalid Input...! Please enter a number between 1 & 6.")
            continue

        print(f"=> Computer Chooses : {com_r}")

        if play_r == com_r:
            print("\n~~~> Computer is OUT...! <~~~")
            break
        else:
            score += com_r
            print(f"===> Computer's Current Score : {score}. <===")

        if traget and score > traget:
            print(f"\n==> Computer chased the target...! Computer's final score : {score}")
            break

    return score

def HandCricket():
    print("\n~=~=~=~=~=~=~> Welcome to Hand Cricket <~=~=~=~=~=~=~")

    play_c = toss()
    if play_c == "exit":
        print("\n===> Game exited. Goodbye...! <===")
        HandCricket()
        return

    if play_c == 'bat':
        print("\n==> You are batting first.")
        play_s = player_batting()
        if play_s == "exit":
            print("\n===> Game exited. Goodbye...! <===")
            HandCricket()
            return
        print(f"\n===> Your total score : {play_s}")
        print("\n==> Now the computer will bet.")
        com_s = computer_batting(traget = play_s)

    else:
        print("\n==> Computer is batting first.")
        com_s = computer_batting()
        if com_s == "exit":
            print("\n===> Game exited. Goodbye...! <===")
            HandCricket()
            return
        print(f"\n===> Computer's total score : {com_s}")
        print("\n==> Now you will bat.")
        play_s = player_batting()

    if play_s > com_s:
        print(f"\n~~~> Congratulations! You won by {play_s - com_s} runs...!")
    elif play_s < com_s:
        print(f"\n---> Computer won by {com_s - play_s} runs. Better luck next time...!")
    else:
        print("\n>>> It's a tie...! <<<")

#GuessCity
stateCapital = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata"
}

def question(stateCapital):
    question = []
    state = list(stateCapital.keys())
    
    for s in random.choice(state, 10):
        correct = stateCapital[s]
        option = [correct]

        while len(option) < 3:
            wrong = random.choice(list(stateCapital.values()))
            if wrong not in option:
                option.append(wrong)

        random.shuffle(option)
            
        question.append((state, correct, wrong))

    return question
    
def validOption():
    while True:
        user_input = input("Select Option (1, 2, 3) : ")
        if user_input in ['1', '2', '3']:
            return int(user_input)
        else:
            print("Invalid Input. Enter only 1, 2, 3.")

def GuessCity():
    ques = question(stateCapital)
    score = 0

    for i in range(len(ques)):
        state, correct, option = ques[i]
        print(f"\nQuestion {i+1} : What is the capital of {state}?")

        op = ['1', '2', '3']
        for i in range(len(option)):
            print(f"{op[i]}. {option[i]}")

        ans = validOption()

        if option[ans - 1] == correct:
            score += 4
            print("Correct...!")
        else:
            score -= 1
            print("Wrong...!")
    
    print("\nQuiz Over...!")
    print(f"Your score : {score} / 40")

#TicTacToe
def print_board(board):
    print("\n")
    print(f" {board[0] if board[0] != ' ' else 1} | {board[1] if board[1] != ' ' else 2} | {board[2] if board[2] != ' ' else 3} ")
    print("---|---|---")
    print(f" {board[3] if board[3] != ' ' else 4} | {board[4] if board[4] != ' ' else 5} | {board[5] if board[5] != ' ' else 6} ")
    print("---|---|---")
    print(f" {board[6] if board[6] != ' ' else 7} | {board[7] if board[7] != ' ' else 8} | {board[8] if board[8] != ' ' else 9} ")
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    return all([spot != ' ' for spot in board])

def TicTacToe():
    board = [' ' for _ in range(9)]
    current_player = 'X'

    while True:
        print_board(board)
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

        if board[move] == ' ':
            board[move] = current_player
        else:
            print("\nThat spot is already taken. Try again.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

def game_zone():

    while True:
        print("\n~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~")
        print("~=~=~=~=~=~=~> Welcome to Game Zone. <~=~=~=~=~=~=~")
        print("~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~")

        valid_enter = ['1', '2', '3', '4','5','6', 'exit']
        user_input = input("""\n====> Enter '1' to play Guess Number Game (0 to 9).\n====> Enter '2' to play Guess Number Game (0 to 100).\n====> Enter '3' to play Rock Papaer Scissor.\n====> Enter '4' to play Hand Cricket.\n====> Enter '5' to play Guess the City.\n====> Enter '6' to play Tic-Tac-Toe.\n====> Enter 'exit' to Quit any game.
                        \n\n====> Enter Here : """)
        
        while user_input not in valid_enter:
            user_input = input("""\n====> Enter '1' to play Guess Number Game (0 to 9).\n====> Enter '2' to play Guess Number Game (0 to 100).\n====> Enter '3' to play Rock Papaer Scissor.\n====> Enter '4' to play Hand Cricket.\n====> Enter '5' to play Guess the City.\n====> Enter '6' to play Tic-Tac-Toe.\n====> Enter 'exit' to Quit any game.
                            \n\n====> Enter Here : """)
        
        if user_input == '1':
            GuessNumber0to9()
            print("\n\nThank you, for playing.")
            break

        elif user_input == '2':
            GuessNumber0to100()
            print("\n\nThank you, for playing.")
            break

        elif user_input == '3':
            RockPaperScissor()
            print("\n\nThank you, for playing.")
            break

        elif user_input == '4':
            HandCricket()
            print("\n\nThank you, for playing.")
            break
        
        elif user_input == '5':
            GuessCity()
            print("\n\nThank you, for playing.")
            break

        elif user_input == '6':
            TicTacToe()
            print("\n\nThank you, for playing.")
            break

        else:
            print("\n\nThank you...!")
            break

game_zone()