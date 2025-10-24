import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


print(
    '''
                          .-------.
                         ___________
                                  /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-''\'---------'' '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
)

bidders = {}
bidding_finished = False
while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bidders[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue.lower() == "no":
        bidding_finished = True
        highest_bidder = ""
        highest_price = 0
        for bidder in bidders:
            bid_amount = bidders[bidder]
            if bid_amount > highest_price:
                highest_price = bid_amount
                highest_bidder = bidder
        print(f"The winner is {highest_bidder} with a bid of ${highest_price}")
    elif should_continue.lower() == "yes":
        clear()
