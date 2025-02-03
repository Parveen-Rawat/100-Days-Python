# Day :9 -- Project -- Blind auction 
import random
def max_bid(dictionary):
    winner = ""
    max = 0
    for prize in dictionary:
        bid_amount = dictionary[prize]
        if bid_amount > max:
            max = bid_amount
            winner = prize
            
            
    print(f"The highest bid was : {winner} with the bidding amount of {max}")

auction_items = ["Vase", "Fruit", "Apple"]

print(f"The auction item is {random.choice(auction_items)}")

statement = True

bids = {}
while statement:
    Name = input("What's your name : ")
    Bid = int(input("What's your bidding price : $"))
    
    bids[Name] = Bid
    print("Do you want to continue\n")
    var = input("If yes then type [y] and if not then [n]").lower()
    
    if var == 'y':
        print("\n"*200)
        statement = True
    else:
        max_bid(bids)
        statement = False