import random
import time

# ============================================================
# MINI ARCADE - PYTHON BASICS VERSION
# Uses only the standard library (random, time) - no pygame
# ============================================================

WORDS = [
    "python", "variable", "function", "arcade", "keyboard",
    "monitor", "package", "monsoon", "elephant", "guitar",
    "planet", "bicycle", "diamond", "compiler", "network",
    "pyramid", "jungle", "cricket"
]

player_name = ""
coins = 0
games_played = 0


# ============================================================
# COMMON FUNCTIONS
# ============================================================

def setup_player():
    global player_name
    while player_name == "":
        player_name = input("Enter your name: ").strip()
        if player_name == "":
            print("Please enter a name.")


def add_coins(amount):
    global coins
    coins += amount


def finish_game():
    global games_played
    games_played += 1


def show_header(title):
    print("\n" + "=" * 45)
    print(title)
    print("=" * 45)


# ============================================================
# GAME 1 - NUMBER GUESSING
# ============================================================

def number_guessing():
    show_header("NUMBER GUESSING")
    print("1. Easy   - 1 to 50, 8 guesses")
    print("2. Medium - 1 to 100, 7 guesses")
    print("3. Hard   - 1 to 500, 9 guesses")
    choice = input("Choose difficulty: ")

    if choice == "2":
        top, tries, prize = 100, 7, 10
    elif choice == "3":
        top, tries, prize = 500, 9, 20
    else:
        top, tries, prize = 50, 8, 5

    secret = random.randint(1, top)
    attempts = 0
    print("\nI have selected a number from 1 to", top)

    while attempts < tries:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if guess < 1 or guess > top:
            print("Keep your guess between 1 and", top)
            continue

        attempts += 1

        if guess == secret:
            print("Correct! You won in", attempts, "attempts.")
            add_coins(prize)
            print("+", prize, "coins")
            finish_game()
            return

        print("Too low!" if guess < secret else "Too high!")

        if abs(guess - secret) <= max(2, top // 50):
            print("You are very close!")

        print("Attempts left:", tries - attempts)

    print("Game over! The number was", secret)
    finish_game()


# ============================================================
# GAME 2 - ROCK PAPER SCISSORS
# ============================================================

def rock_paper_scissors():
    show_header("ROCK PAPER SCISSORS")
    print("First player to reach 3 points wins.")

    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    while player_score < 3 and computer_score < 3:
        player = input("Choose rock, paper or scissors: ").lower()

        if player not in choices:
            print("Invalid choice.")
            continue

        computer = random.choice(choices)
        print("Computer chose:", computer)

        if player == computer:
            print("Draw!")
        elif (
            (player == "rock" and computer == "scissors")
            or (player == "paper" and computer == "rock")
            or (player == "scissors" and computer == "paper")
        ):
            player_score += 1
            print("You win this round!")
        else:
            computer_score += 1
            print("Computer wins this round!")

        print("Score:", player_score, "-", computer_score)

    if player_score == 3:
        print("You won the game! +15 coins")
        add_coins(15)
    else:
        print("Computer won the game.")

    finish_game()


# ============================================================
# GAME 3 - HANGMAN
# ============================================================

def hangman():
    show_header("HANGMAN")
    word = random.choice(WORDS)
    guessed = []
    wrong = 0
    max_wrong = 6

    while wrong < max_wrong:
        shown = "".join(letter + " " if letter in guessed else "_ " for letter in word)
        print("\nWord:", shown)
        print("Wrong guesses:", wrong, "/", max_wrong)

        if all(letter in guessed for letter in word):
            print("You guessed the word!")
            print("+20 coins")
            add_coins(20)
            finish_game()
            return

        letter = input("Guess a letter: ").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Enter one letter only.")
            continue

        if letter in guessed:
            print("You already guessed that letter.")
            continue

        guessed.append(letter)

        if letter in word:
            print("Correct!")
        else:
            wrong += 1
            print("Wrong guess!")

    print("\nYou lost. The word was:", word)
    finish_game()


# ============================================================
# GAME 4 - TIC TAC TOE
# ============================================================

def display_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def winner(board):
    win_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in win_lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def computer_ttt_move(board):
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if winner(board) == "O":
                board[i] = " "
                return i
            board[i] = " "

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if winner(board) == "X":
                board[i] = " "
                return i
            board[i] = " "

    for i in [4, 0, 2, 6, 8, 1, 3, 5, 7]:
        if board[i] == " ":
            return i
    return None


def tic_tac_toe():
    show_header("TIC TAC TOE")
    board = [" "] * 9

    while True:
        display_board(board)
        try:
            position = int(input("Choose a position (1-9): ")) - 1
        except ValueError:
            print("Enter a number from 1 to 9.")
            continue

        if position < 0 or position > 8 or board[position] != " ":
            print("Invalid or occupied position.")
            continue

        board[position] = "X"

        if winner(board) == "X":
            display_board(board)
            print("You won! +25 coins")
            add_coins(25)
            finish_game()
            return

        if " " not in board:
            display_board(board)
            print("It's a draw! +5 coins")
            add_coins(5)
            finish_game()
            return

        computer_position = computer_ttt_move(board)
        if computer_position is not None:
            board[computer_position] = "O"

        if winner(board) == "O":
            display_board(board)
            print("Computer wins.")
            finish_game()
            return

        if " " not in board:
            display_board(board)
            print("It's a draw! +5 coins")
            add_coins(5)
            finish_game()
            return


# ============================================================
# GAME 5 - MATH SPRINT
# ============================================================

def make_math_question():
    a = random.randint(2, 20)
    b = random.randint(2, 12)
    operation = random.choice(["+", "-", "*"])

    if operation == "+":
        answer = a + b
    elif operation == "-":
        if a < b:
            a, b = b, a
        answer = a - b
    else:
        answer = a * b

    return a, b, operation, answer


def math_sprint():
    show_header("MATH SPRINT")
    total_questions = 8
    score = 0
    start_time = time.time()

    for question_number in range(1, total_questions + 1):
        a, b, operation, answer = make_math_question()
        print("\nQuestion", question_number, "of", total_questions)
        print("What is", a, operation, b, "?")

        try:
            user_answer = int(input("Answer: "))
        except ValueError:
            print("Invalid answer. Counted as wrong.")
            user_answer = None

        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong! Correct answer:", answer)

    elapsed = round(time.time() - start_time, 1)
    print("\nFinal score:", score, "/", total_questions)
    print("Time:", elapsed, "seconds")

    if score == 8:
        prize = 30
    elif score >= 6:
        prize = 15
    elif score >= 4:
        prize = 5
    else:
        prize = 0

    if prize > 0:
        add_coins(prize)
        print("+", prize, "coins")
    else:
        print("No coins this time.")

    finish_game()


# ============================================================
# GAME 6 - WORD SCRAMBLE
# ============================================================

def scramble_word(word):
    letters = list(word)
    for _ in range(10):
        random.shuffle(letters)
        scrambled = "".join(letters)
        if scrambled != word:
            return scrambled
    return scrambled


def word_scramble():
    show_header("WORD SCRAMBLE")
    word = random.choice(WORDS)
    puzzle = scramble_word(word)
    lives = 3

    print("Unscramble this word:", puzzle)

    while lives > 0:
        guess = input("Your answer: ").strip().lower()

        if guess == "":
            print("Type an answer.")
            continue

        if guess == word:
            prize = lives * 10
            print("Correct! +", prize, "coins")
            add_coins(prize)
            finish_game()
            return

        lives -= 1

        if lives > 0:
            revealed = len(word) - lives
            print("Wrong!")
            print("Hint:", word[:revealed])
            print("Tries left:", lives)
        else:
            print("Out of tries.")
            print("The word was:", word)

    finish_game()


# ============================================================
# GAME 7 - MEMORY SEQUENCE
# ============================================================

def memory_sequence():
    show_header("MEMORY SEQUENCE")
    sequence = []
    round_number = 0

    while True:
        round_number += 1
        sequence.append(str(random.randint(0, 9)))

        print("\nRound", round_number)
        print("Remember this sequence:")
        print(" ".join(sequence))

        time.sleep(2)
        print("\n" * 30)

        answer = input("Enter the sequence: ").replace(" ", "")
        correct = "".join(sequence)

        if answer == correct:
            print("Correct!")
            print("Next round...")
        else:
            coins_earned = (round_number - 1) * 5
            print("\nWrong!")
            print("Correct sequence:", " ".join(sequence))
            print("You reached round", round_number)

            if coins_earned > 0:
                add_coins(coins_earned)
                print("+", coins_earned, "coins")

            finish_game()
            return


# ============================================================
# GAME 8 - SPACE SHOOTER (TEXT VERSION)
# Turn-based, grid drawn with plain text. No pygame needed.
# ============================================================

def space_shooter():
    show_header("SPACE SHOOTER (TEXT)")
    print("Controls: a=left, d=right, f=fire, s=stay, q=quit")

    width = 7
    height = 6
    player_pos = width // 2
    lives = 3
    score = 0
    enemies = []   # each item: [col, row]
    bullets = []   # each item: [col, row]
    turn = 0

    def draw():
        grid = [["." for _ in range(width)] for _ in range(height)]

        for col, row in enemies:
            if 0 <= row < height:
                grid[row][col] = "V"

        for col, row in bullets:
            if 0 <= row < height:
                grid[row][col] = "|"

        print()
        for row in grid:
            print(" ".join(row))

        ship_line = ["." for _ in range(width)]
        ship_line[player_pos] = "^"
        print(" ".join(ship_line))
        print("Score:", score, " Lives:", lives)

    while lives > 0:
        turn += 1
        draw()
        move = input("Move: ").lower().strip()

        if move == "q":
            break

        if move == "a" and player_pos > 0:
            player_pos -= 1
        elif move == "d" and player_pos < width - 1:
            player_pos += 1
        elif move == "f":
            bullets.append([player_pos, height - 2])

        bullets = [[c, r - 1] for c, r in bullets if r - 1 >= 0]
        enemies = [[c, r + 1] for c, r in enemies]

        if turn % 2 == 0:
            enemies.append([random.randint(0, width - 1), 0])

        remaining_enemies = []
        remaining_bullets = bullets[:]

        for enemy in enemies:
            hit = False

            for bullet in remaining_bullets[:]:
                if enemy[0] == bullet[0] and enemy[1] == bullet[1]:
                    remaining_bullets.remove(bullet)
                    hit = True
                    score += 10
                    break

            if not hit:
                remaining_enemies.append(enemy)

        enemies = remaining_enemies
        bullets = remaining_bullets

        survivors = []
        for enemy in enemies:
            if enemy[1] >= height - 1:
                lives -= 1
                if enemy[0] == player_pos:
                    print("Direct hit! Lives left:", lives)
                else:
                    print("An enemy got through! Lives left:", lives)
            else:
                survivors.append(enemy)
        enemies = survivors

    print("\nGame over! Final score:", score)
    prize = score // 2

    if prize > 0:
        add_coins(prize)
        print("+", prize, "coins")

    finish_game()


# ============================================================
# MAIN MENU
# ============================================================

def show_menu():
    print("\n")
    print("=" * 45)
    print("              🎮 MINI ARCADE")
    print("=" * 45)
    print("Player:", player_name)
    print("Coins:", coins)
    print("Games played:", games_played)
    print()
    print("1. Number Guessing")
    print("2. Rock Paper Scissors")
    print("3. Hangman")
    print("4. Tic Tac Toe")
    print("5. Math Sprint")
    print("6. Word Scramble")
    print("7. Memory Sequence")
    print("8. Space Shooter")
    print("9. Player Stats")
    print("10. Exit")
    print("=" * 45)


def player_stats():
    show_header("PLAYER STATS")
    print("Player name :", player_name)
    print("Coins       :", coins)
    print("Games played:", games_played)


def main():
    setup_player()

    games = {
        "1": number_guessing,
        "2": rock_paper_scissors,
        "3": hangman,
        "4": tic_tac_toe,
        "5": math_sprint,
        "6": word_scramble,
        "7": memory_sequence,
        "8": space_shooter,
    }

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice in games:
            games[choice]()
        elif choice == "9":
            player_stats()
        elif choice == "10":
            print("\nThanks for playing,", player_name + "!")
            print("Final coins:", coins)
            print("Games played:", games_played)
            break
        else:
            print("Invalid choice. Please select 1-10.")


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":
    main()
