import os
bids ={}

def process_input():
    name = input("What is your name?: ")
    bid = float(input("What's your bid?: $"))
    bids[name] = bid

choice = "yes"
while choice == "yes":
    process_input()
    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    os.system('cls' if os.name == 'nt' else 'clear')

winner = ""
max_bid = -1
for name,bid in bids.items():
    if bid > max_bid:
        winner = name
        max_bid = bid

print(f"The winner is {winner} with a bid of ${max_bid}")