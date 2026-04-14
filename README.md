<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Slot Machine Game

A simple command-line slot machine game where players deposit money, choose how many lines to bet on, and spin the reels to win or lose credits based on random outcomes.[^1][^2]

## Features

- Text-based interactive interface in the terminal.[^1]
- Customizable number of betting lines (1–3).[/file:2]
- Configurable minimum and maximum bet per line.[^2]
- Randomized 3x3 slot machine grid using weighted symbols.[^2]
- Automatic calculation of winnings and display of winning lines.[^2]


## How It Works

- The player starts by entering an initial deposit amount.[^1][^2]
- For each round, the player chooses how many lines to bet on and how much to bet per line, within allowed limits.[^2]
- The game generates a random 3x3 grid of symbols, prints it, and calculates winnings based on matching symbols across each active line.[^2]
- The player’s balance is updated by adding the net result of the spin (winnings minus total bet), and they can continue playing or quit.[^1][^2]


## Requirements

- **Python** 3.7 or later (no third-party dependencies required).[^1][^2]

The game uses only the standard library (`random` and `input/print`).[^2]

## Installation

1. Clone or download this project to your local machine.[^1]
2. Ensure both `app.py` and `utils.py` are in the same directory.[^1][^2]
3. Verify you have Python 3 installed by running `python --version` or `python3 --version` in your terminal.[^1]

## Running the Game

From the project directory, run:

```bash
python app.py
```

or, depending on your environment:

```bash
python3 app.py
```

This starts the main loop defined in `app.app()`, which manages the deposit, repeated spins, and exit condition.[^1]

## Game Rules

- **Deposit**:
    - You must deposit a positive integer amount to start playing.[^2]
- **Lines**:
    - You can bet on 1 to 3 lines per spin.[^2]
    - Lines are horizontal rows in the 3x3 grid (top, middle, bottom).[^2]
- **Bets**:
    - Minimum bet per line: 1.[^2]
    - Maximum bet per line: 150.[^2]
    - Total bet = bet per line × number of lines; it cannot exceed your current balance.[^2]
- **Symbols and Payouts**:
    - The slot machine uses symbols `A`, `B`, `C`, `D` with different frequencies and values.[^2]
    - Each winning line pays `symbol_value * bet`, where `symbol_value` is higher for rarer symbols.[^2]
- **Winning Condition**:
    - A line wins if all three symbols in that row across the columns match (e.g., `A A A`).[^2]
    - Multiple lines can win in a single spin; total winnings are the sum of all winning lines.[^2]


## Project Structure

```text
.
├── app.py      # Entry point; handles main game loop and balance tracking
└── utils.py    # Core game logic (spins, winnings, input validation)
```

- `app.py`
    - Imports `utils` and runs the main **app** function when executed as a script.[^1]
    - Handles balance initialization via `utils.deposit()` and per-round updates via `utils.spin(balance)`.
- `utils.py`
    - Contains constants for rows, columns, max/min bets, and symbol configuration.[^2]
    - Implements helper functions:
        - `deposit()` – get and validate initial deposit from the user.[^2]
        - `get_number_of_lines()` – choose number of lines to bet on.[^2]
        - `get_bet()` – choose per-line bet within allowed range.[^2]
        - `get_slot_machine_spin()` – generate a random 3x3 symbol grid based on symbol frequencies.[^2]
        - `print_slot_machine()` – print the grid in a readable format.[^2]
        - `check_winnings()` – compute total winnings and identify winning lines.[^2]
        - `spin(balance)` – orchestrate a single round using all the above utilities and return the net change.[^2]


## Example Session

1. Run `python app.py`.[^1]
2. Enter a deposit amount, e.g., `500`.[^2]
3. Choose number of lines, e.g., `3`.[^2]
4. Enter bet per line, e.g., `10` (total bet = 30).[^2]
5. View the printed 3x3 grid, your winnings, and the updated balance.[^2]
6. Press Enter to spin again or `q` to quit.[^1]

## Possible Improvements

- Add input validation for non-integer or very large deposits/bets beyond current checks.[^2]
- Support configurable symbol sets, paylines, and payout tables via a configuration file.[^2]
- Implement a simple statistics screen (total spins, total winnings, max win, etc.).[^2]
- Add tests for `check_winnings` and `get_slot_machine_spin` to ensure consistent behavior.[^2]

<div align="center">⁂</div>

[^1]: app.py

[^2]: utils.py

