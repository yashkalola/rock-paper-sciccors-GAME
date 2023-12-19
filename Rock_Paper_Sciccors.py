from random import randint

t = ["Rock", "Paper", "Sciccors"]
player_move = ""
computer_move = ""
Number_of_tie = 0
player_point = 0
computer_point = 0
emojis = {"Rock": "✊", "Paper": "✋", "Sciccors": "✌"}

print('To exit the game type "exit"')

while player_move != "exit":
    player_move = input("Rock, Paper, Sciccors? ")
    computer_move = t[randint(0, 2)]
    if player_move == computer_move:
        Number_of_tie += 1
        print("You Choose:", emojis[player_move])
        print("Computer Choose:", emojis[computer_move])
        print("Tie!")
    elif player_move == "Rock":
        if computer_move == "Paper":
            print("You Choose:", emojis[player_move])
            print("Computer Choose:", emojis[computer_move])
            print("Computer Win!")
            print("Paper covers Rock")
            computer_point += 1
        elif computer_move == "Sciccors":
            print("You Choose:", emojis[player_move])
            print("Computer Choose:", emojis[computer_move])
            print("You Win!")
            print("Rock smashes Sciccors")
            player_point += 1

    elif player_move == "Paper":
        if computer_move == "Rock":
            print("You Choose:", emojis[player_move])
            print("Computer Choose:", emojis[computer_move])
            print("You Win!")
            print("Paper Covers Rock")
            player_point += 1
        elif computer_move == "Sciccors":
            print("You Choose:", emojis[player_move])
            print("Computer Choose:", emojis[computer_move])
            print("Computer Win!")
            print("Sciccors cuts Paper")
            computer_point += 1
    elif player_move == "Sciccors":
        if computer_move == "Rock":
            print("You Choose:", emojis[player_move])
            print("Computer Choose:", emojis[computer_move])
            print("Computer Win!")
            print("Rock smashes Sciccors")
            computer_point += 1
        elif computer_move == "Paper":
            print("You Choose:", emojis[player_move])
            print("Computer Choose:", emojis[computer_move])
            print("You Win!")
            print("Sciccors cuts Paper")
            player_point += 1
    elif player_move == "exit":
        print("your point:", player_point)
        print("computer point:", computer_point)
        print("Number of Ties:", Number_of_tie)
        if player_point > computer_point:
            print("You Win!")
        elif player_point < computer_point:
            print("Computer Win!")
        elif player_point == computer_point:
            print("Both players point are same It's Tie")
    else:
        print("That's not valid play, Please Check your spelling!")
    
