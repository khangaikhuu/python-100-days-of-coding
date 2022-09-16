cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random
def deal_card():
 """ Returns a random card from the deck. """
 card = random.choice(cards)
 return card

print(deal_card())


user_cards = []

computer_cards = []


for _ in range(2):
 user_cards.append(deal_card())
 computer_cards.append(deal_card())
 

print(user_cards)
print(computer_cards)


def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
   return 0
  if 11 in cards and sum(cards) > 21:
   cards.remove(11)
   cards.append(1)
   
  return sum(cards)
  
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(user_score)
print(computer_score)

if user_score == 0 or computer_score == 0 or user_score > 21:
 is_game_over = True
else:
 user_should_deal = input("Type 'y' to get another card type 'n' to pass:")
 if user_should_deal == "y":
  user_cards.append(deal_card())
 else:
  is_game_over = True

print(user_cards)
print(computer_cards)
