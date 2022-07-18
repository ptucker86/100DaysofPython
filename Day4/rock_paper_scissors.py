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

#Write your code below this line 👇
game_images =  [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))
computer_choice = random.randint(0,2)
print("3...2...1...shoot")

if user_choice < 3 or user_choice >=0:
    print(game_images[user_choice])
else:
    print("You're going to lose with that choice.")

print(game_images[computer_choice])

original_code = '''
if user_choice == 0:
    print("Your choice: rock")
    print(rock)
elif user_choice == 1:
    print("Your choice: paper")
    print(paper)
elif user_choice == 2:
    print("Your choice: scissors")
    print(scissors)
else:
    print("You're going to lose with that choice.")
'''

original_code_2 = '''
if computer_choice == 0:
    print("Computer choice: rock")
    print(rock)
elif computer_choice == 1:
    print("Computer choice: paper")
    print(paper)
elif computer_choice == 2:
    print("Computer choice: scissors")
    print(scissors)
'''


if user_choice == computer_choice:
    print("It's a draw")
elif user_choice >= 3 or user_choice < 0:
    print("Your choice was invalid so you lose.")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 2 and computer_choice == 0:
    print("Computer wins")
elif user_choice < computer_choice:
    print("Computer wins")
elif user_choice > computer_choice:
    print("You win")
