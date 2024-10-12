# THIS IS THE D9 PROJECT
# MAKING THE SECRET AUCTION PROGRAM
# THIS FOCUSES ON DICTIONARY

from art import logo

bidding_list = {}

while True:
    print(logo)
    print("Welcome to:\nTHE SECRET AUCTION PROGRAM!\n")

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bidding_list[name] = bid
    prompt = input("\nAre there other users who want to bid? yes or no: ").lower()
    if prompt == "yes":
        print("\n" * 100)
    elif prompt == "no":
        break



highest_bid = -1
highest_bid_name = ""
for name in bidding_list:
    if bidding_list[name] > highest_bid:
        highest_bid = bidding_list[name]
        highest_bid_name = name
    
print(f"\nThe winner is {highest_bid_name} with a bid of ${highest_bid}")

# Can also use this to get the key of the highest value in a dictionary
n = max(bidding_list, key=bidding_list.get)
print(n)
print(bidding_list[n])