import art


def add_value():
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: "))
    players[name] = bid

    add_person = input("Is there any other person plays? (yes/no): ")
    if add_person == "yes":
        add_value()
    else:
        find_winner()


def find_winner():
    winner = ""
    biggest_bid = 0
    for key in players:
        if biggest_bid < players[key]:
            biggest_bid = players[key]
            winner = key
    print(f"The winner is {winner} with {biggest_bid}")


print(art.logo)
players = {}
print("Welcome to auction!")
add_value()
