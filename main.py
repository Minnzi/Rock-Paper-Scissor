rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
import os
game_is_on = True

game_images = [rock, paper, scissors]

while game_is_on:
    computer_choice = random.randint(0, 2)
    user_choice = int(
        input(
            "What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"
        ))
    if user_choice >= 3 or user_choice < 0:
        print("You have entered an invalid input.")
    else:
        print(game_images[user_choice])
        print("Computer chose:")
        print(game_images[computer_choice])

        if user_choice == computer_choice:
            print("It's a draw.")
        elif user_choice > computer_choice and (user_choice + computer_choice) != 2:
            print("You win!")
        elif user_choice == 0 and computer_choice == 2:
            print("You win!")
        else:
            print("You lose.")
    if input("Do you want to play again? Type 'y' or 'n': ").lower() == 'n':
        game_is_on = False
    else:
        os.system('cls')



