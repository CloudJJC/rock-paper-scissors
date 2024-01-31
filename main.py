import time
import random

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


print("Welcome to the Rock, Paper, Scissors game!")

time.sleep(1) 

images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("You chose:")
if user_choice >= 3 or user_choice < 0:
  print("Invalid choice. You lose!")
else:
  print(images[user_choice])

  computer_choice = random.randint(0,2)
  print("The computer chose:")
  print(images[computer_choice])


  # Human wins scenerio 
  if user_choice == 0 and computer_choice == 2:
    print("Woohoo! You win!!")
  elif user_choice == 2 and computer_choice == 1:
    print("Woohoo! You win!!")
  elif user_choice == 1 and computer_choice == 0:
    print("Woohoo! You win!!")
  # Draw scenerio
  elif user_choice == computer_choice:
    print("It's a draw! Repeate the game!")
  # Computer wins scenerio
  elif computer_choice == 0 and user_choice == 2:
    print("Ouch! You lose!")
  elif computer_choice == 2 and user_choice == 1:
    print("Ouch! You lose!")
  elif computer_choice == 1 and user_choice == 0:
    print("Ouch! You lose!")