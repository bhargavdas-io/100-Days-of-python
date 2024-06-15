def clear():
    import os
    os.system('cls')

from auction_logo import logo
print(logo)


bids = {}
bid_finish = False
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bid_finish:
    name_input = input("What is your name?: ")
    bid_amount = int(input("What's your bid amount?:$ "))
    bids[name_input] = bid_amount
    rerun = input("Are there other users who want to bid? Type 'yes' or 'no'\n")
    if rerun == 'no':
        bid_finish = True
        find_highest_bidder(bids)
    elif rerun == 'yes':
        clear()
