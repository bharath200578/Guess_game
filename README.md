# 🎯 Number Guessing Game (Python)

A simple command-line Number Guessing Game built using Python. The computer randomly selects a number between 1 and 100, and the player must guess the correct number based on hints provided by the game.

## 🚀 Features

- Random number generation.
- Three difficulty levels:
  - Easy: 10 attempts
  - Medium: 5 attempts
  - Hard: 3 attempts
- Input validation for difficulty selection.
- Exception handling using `try-except`.
- Prevents invalid guesses from consuming attempts.
- Provides hints to help players guess the number.
- Displays the correct answer when the player runs out of attempts.

## 🛠️ Technologies Used

- Python 3
- Random module
- Exception Handling
- Loops and Conditional Statements
- Functions

## 📂 Project Structure

```text
number-guessing-game/
│
└── main.py
```

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/bharath200578/Guess_game.git
```

**2. Run the game**

```bash
python number_guessing_game.py
```

## 🎮 How to Play

1. Run the Python file.
2. Select your preferred difficulty level.
3. Enter a number between 1 and 100.
4. Follow the hints:
   - If your guess is too low, the game tells you to guess higher.
   - If your guess is too high, the game tells you to guess lower.
5. Guess the correct number before running out of attempts!

## 📸 Example Output

```text
Welcome to the Number Guessing Game!

I'm thinking of a number between 1 and 100.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: 2

You selected difficulty level 2.
Let's start the game!

Attempt 1/5: Enter your guess: 40
Incorrect! The number is greater than 40.

Attempt 2/5: Enter your guess: 70
Incorrect! The number is less than 70.

Attempt 3/5: Enter your guess: 55

Congratulations! You guessed it in 3 attempts.
```

## 📚 Concepts Practiced

This project helped me practice:

- Python variables and data types.
- Random number generation.
- `if-elif-else` statements.
- `for` and `while` loops.
- Nested loops.
- Functions.
- Exception handling (`try-except`).
- Input validation.
- Loop `else` statements.

## 🔮 Future Improvements

- Add a Play Again option.
- Track the best score.
- Display remaining attempts.
- Use dictionaries to manage difficulty levels.

---

**Author:** Bharath

ROADMAP.sh 
https://roadmap.sh/projects/number-guessing-game

Built as a Python practice project to strengthen programming fundamentals and logical thinking.
