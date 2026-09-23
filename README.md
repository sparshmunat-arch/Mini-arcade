(+, −, ×) against the clock; your score determines the coin payout. |
| 6 | **Word Scramble** | Unscramble a shuffled word within # 🎮 Mini Arcade — Python Basics Version

A single-file, terminal-based arcade of eight small games, built with **only the Python standard library** (`random` and `time` — no external packages, no pygame).

## Requirements

- Python 3.6+
- No installation needed — just the two standard library modules `random` and `time`

## How to Run

```bash
python mini_arcade_python_basics_final.py
```

You'll be asked for your name, then dropped into the main menu.

## Games

| # | Game | Description |
|---|------|-------------|
| 1 | **Number Guessing** | Guess a secret number within a limited number of tries. Choose Easy (1–50), Medium (1–100), or Hard (1–500) — harder difficulties pay more coins. |
| 2 | **Rock Paper Scissors** | Best-of, first to 3 points beats the computer. |
| 3 | **Hangman** | Guess the hidden word one letter at a time before running out of wrong guesses (6 max). |
| 4 | **Tic Tac Toe** | Play against a computer opponent that blocks your winning moves and takes its own when available. |
| 5 | **Math Sprint** | Answer 8 quick arithmetic questions 3 lives; fewer wrong guesses = more coins, with letter hints revealed as lives run out. |
| 7 | **Memory Sequence** | Memorize a growing sequence of digits and type it back correctly each round; payout scales with how far you get. |
| 8 | **Space Shooter (Text)** | A turn-based, ASCII-grid shooter — move left/right, fire, and shoot down incoming enemies before they reach you. |

Plus:
- **Player Stats** — view your name, coin total, and games played
- **Exit** — ends the session with a final summary

## Game Loop & Scoring

- All games run through a shared `games` dictionary keyed by menu number, called from `main()`.
- Coins are tracked in a global `coins` variable via `add_coins()`, and each completed game increments `games_played` via `finish_game()`.
- Progress (coins, games played) persists only for the current run — nothing is saved to disk.

## Code Structure

```
mini_arcade_python_basics_final.py
├── Shared state & helpers      (player_name, coins, games_played, setup_player, add_coins, finish_game, show_header)
├── Game 1: number_guessing()
├── Game 2: rock_paper_scissors()
├── Game 3: hangman()
├── Game 4: tic_tac_toe()        (+ display_board, winner, computer_ttt_move)
├── Game 5: math_sprint()        (+ make_math_question)
├── Game 6: word_scramble()      (+ scramble_word)
├── Game 7: memory_sequence()
├── Game 8: space_shooter()
├── show_menu() / player_stats()
└── main()                       (entry point)
```

## Notes

- This was built as a Python fundamentals practice project — the code favors readability (loops, conditionals, functions, basic data structures) over advanced techniques.
- Word-based games (Hangman, Word Scramble) draw from a fixed `WORDS` list of 18 words.
