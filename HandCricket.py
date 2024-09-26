import random

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

HandCricket()