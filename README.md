# Slot Machine Game

A simple command-line slot machine game where players deposit money, choose how many lines to bet on, and spin the reels to win or lose credits based on random outcomes.

## Features

- Text-based interactive interface in the terminal.
- Customizable number of betting lines (1–3).
- Configurable minimum and maximum bet per line.
- Randomized 3x3 slot machine grid using weighted symbols.
- Automatic calculation of winnings and display of winning lines.


## How It Works

- The player starts by entering an initial deposit amount.
- For each round, the player chooses how many lines to bet on and how much to bet per line, within allowed limits.
- The game generates a random 3x3 grid of symbols, prints it, and calculates winnings based on matching symbols across each active line.
- The player’s balance is updated by adding the net result of the spin (winnings minus total bet), and they can continue playing or quit.


## Requirements

- **Python** 3.7 or later (no third-party dependencies required).

The game uses only the standard library (`random` and `input/print`).

## Installation

1. Clone or download this project to your local machine.
2. Ensure both `app.py` and `utils.py` are in the same directory.
3. Verify you have Python 3 installed by running `python --version` or `python3 --version` in your terminal.

## Running the Game

From the project directory, run:

```bash
python app.py
```

or, depending on your environment:

```bash
python3 app.py
```

This starts the main loop defined in `app.app()`, which manages the deposit, repeated spins, and exit condition.

## Game Rules

- **Deposit**:
    - You must deposit a positive integer amount to start playing.
- **Lines**:
    - You can bet on 1 to 3 lines per spin.
    - Lines are horizontal rows in the 3x3 grid (top, middle, bottom).
- **Bets**:
    - Minimum bet per line: 1.
    - Maximum bet per line: 150.
    - Total bet = bet per line × number of lines; it cannot exceed your current balance.
- **Symbols and Payouts**:
    - The slot machine uses symbols `A`, `B`, `C`, `D` with different frequencies and values.
    - Each winning line pays `symbol_value * bet`, where `symbol_value` is higher for rarer symbols.
- **Winning Condition**:
    - A line wins if all three symbols in that row across the columns match (e.g., `A A A`).
    - Multiple lines can win in a single spin; total winnings are the sum of all winning lines.


## Project Structure

```text
.
├── app.py      # Entry point; handles main game loop and balance tracking
└── utils.py    # Core game logic (spins, winnings, input validation)
```

- `app.py`
    - Imports `utils` and runs the main **app** function when executed as a script.
    - Handles balance initialization via `utils.deposit()` and per-round updates via `utils.spin(balance)`.
- `utils.py`
    - Contains constants for rows, columns, max/min bets, and symbol configuration.
    - Implements helper functions:
        - `deposit()` – get and validate initial deposit from the user.
        - `get_number_of_lines()` – choose number of lines to bet on.
        - `get_bet()` – choose per-line bet within allowed range.
        - `get_slot_machine_spin()` – generate a random 3x3 symbol grid based on symbol frequencies.
        - `print_slot_machine()` – print the grid in a readable format.
        - `check_winnings()` – compute total winnings and identify winning lines.
        - `spin(balance)` – orchestrate a single round using all the above utilities and return the net change.


## Example Session

1. Run `python app.py`.
2. Enter a deposit amount, e.g., `500`.
3. Choose number of lines, e.g., `3`.
4. Enter bet per line, e.g., `10` (total bet = 30).
5. View the printed 3x3 grid, your winnings, and the updated balance.
6. Press Enter to spin again or `q` to quit.

## Possible Improvements

- Add input validation for non-integer or very large deposits/bets beyond current checks.
- Support configurable symbol sets, paylines, and payout tables via a configuration file.
- Implement a simple statistics screen (total spins, total winnings, max win, etc.).
- Add tests for `check_winnings` and `get_slot_machine_spin` to ensure consistent behavior.
