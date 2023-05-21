from replit import clear
import art

print(art.logo)
print("Welcome to the secret auction program.")

name = ""
bid = ""
other_bidders = ""

list_bids = []
bids = {}

def auction(name, bid, other_bidders):
  bids["name"] = name
  bids["bid"] = int(bid)
  #bids["other_bidders"] = other_bidders
  list_bids.append(bids)
  #print(list_bids)

def winner():
  winner_bid = 0
  winner_name = ""
  for n in list_bids:
    if winner_bid < n["bid"]:
      winner_bid = n["bid"]
      winner_name = n["name"]

  print(f"The winner is {winner_name} with a bid of ${winner_bid}")
      
start_again = True
while start_again == True:
  name = input("What is your name?: ")
  bid = input("What's your bid? ")
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  
  auction(name, bid, other_bidders)
  if other_bidders == "no":
    start_again = False
    winner()
  else:
    clear()
    auction(name, bid, other_bidders)
