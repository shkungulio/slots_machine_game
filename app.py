"""
Slot Machine Game
A simple slot machine game where players can deposit money, choose how many lines to bet on, and spin the reels to win or lose money based on the outcome.
"""

import utils 

def app():
    """Run the main interactive game loop.
    Prompts the player for an initial deposit, repeatedly offers a chance to
    play a round, updates the balance after each spin, and exits when the user
    chooses to quit.
    """
    balance = utils.deposit()
    while True:
        message = f"You current balance is ${balance:,.2f}\n"
        print(message)
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += utils.spin(balance)
    print(message)

if __name__ == "__main__":
    app()