import random

choices = ["Rock", "Paper", "Scissors"]

game_on = True
input_is_valid = True

user_score = 0
computer_score = 0

print("If you want to close the game type x")

while game_on:

    user_choice = input("What do you chose? Rock, Paper or Scissors?\n")

    print("You chose " + str(user_choice))

    if user_choice == "x":
        break
    elif user_choice not in choices:
        print("Please type: Rock, Paper, Scissors as you see!")
        input_is_valid = False
    else:
        input_is_valid = True

    if input_is_valid == True:
        computer_choice = random.choice(choices)
        print("Computer chose "+ str(computer_choice))

        if user_choice == "Rock" and computer_choice == "Scissors":
            user_score +=1
            print("You win!")

        elif user_choice == "Scissors" and computer_choice == "Paper":
            user_score +=1
            print("You win!")

        elif user_choice == "Paper" and computer_choice == "Rock":
            user_score +=1
            print("You win!")

        elif user_choice == computer_choice:
            print("Draw")

        else:
            computer_score +=1
            print("You lose!")
    
        print("Your score: " + str(user_score) + " | Computer score: " + str(computer_score))
