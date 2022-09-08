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

your_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors'))
print(your_choice)

game_values = [rock, paper, scissors]
computer_random = random.randint(0,2)
print(computer_random)
computer_choice = game_values[computer_random]
print(game_values[your_choice])
print('\n')
print('Computer chose:\n')
print(computer_choice)
 
if your_choice>= 3 or your_choice < 1:
  print('You typed an invalid number, you lose!')
elif computer_random == 0 and your_choice == 2:
 print('You win')
elif computer_random == 2 and your_choice == 0:
 print('You lose')
elif computer_random > your_choice:
 print('You lose')
elif computer_random < your_choice:
 print('You win')
elif computer_random == your_choice:
 print('It is a draw')
 



