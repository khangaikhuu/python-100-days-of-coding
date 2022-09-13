from art import logo

print(logo)
print('Welcome i\n')

stop_game = False 
bidder = {}

def find_highest_bidder(bidding_record):
 max_bid = 0
 winner = ""
 for key in bidding_record:
  bid_amount = bidding_record[key]
  if bid_amount > max_bid:
   max_bid = bid_amount
   winner = key 
 print(f"The winner is {winner} with a bid of ${max_bid}")
  

while not stop_game:
 name = input('What is your name? ')
 user_bid = int(input('What is your bid? $'))
 bidder[name]=user_bid
 should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
 if should_continue == 'no':
  stop_game = True
  find_highest_bidder(bidder)


  


