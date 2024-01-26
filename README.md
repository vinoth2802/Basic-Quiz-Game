# Quiz Game

This is a simple Python script for a basic quiz game. It allows users to answer multiple-choice questions and provides feedback on their performance. The game is created by Vinothkumar J.

## How to Play

1. Run the script in a Python environment.
2. Answer each question by entering the corresponding letter (A, B, C, or D).
3. After completing all the questions, the script will display your results.

## Code Structure

### `play()` Function

The `play()` function is responsible for displaying questions, options, collecting player answers, and checking their correctness. It uses loops to iterate through the questions and options, providing feedback for each answer.

### `get_results(guesses, correct_guesses)` Function

The `get_results()` function calculates and displays the player's score based on the number of correct guesses. It also compares the player's guesses with the correct answers and provides detailed results.

### `play_again()` Function

The `play_again()` function allows players to choose whether they want to play the quiz again. If the player chooses to play again, the `play()` function is called; otherwise, the script exits.

## Questions and Options

You can easily modify the quiz content without changing the entire code. Update the `questions`, `options`, and `answers` variables with your desired content.

```python
questions = ["1. What is the largest ocean in the world?",
             "2. What is the tallest mountain in the world?",
             "3. What is the chemical formula for water?",
             "4. What is the name of the largest planet in the solar system?"]

options = [{"A": "Atlantic", "B": "Pacific", "C": "Indian", "D": "Arctic"},
           {"A": "Mount Fuji", "B": "Mount Kilimanjaro", "C": "Mount Everest", "D": "Kangchenjunga"},
           {"A": "H₂O", "B": "CO₂", "C": "HCL", "D": "CO₃"},
           {"A": "Earth", "B": "Neptune", "C": "Jupiter", "D": "Saturn"}]

answers = {1: "B", 2: "C", 3: "A", 4: "C"}
```

## Modify the Quiz

Feel free to update the quiz content by modifying the `questions`, `options`, and `answers` variables. This allows you to customize the quiz without altering the core functionality of the code.

```python
# Example of modification:
questions[0] = "1. What is the capital of France?"
options[0] = {"A": "Berlin", "B": "Paris", "C": "Madrid", "D": "Rome"}
answers[1] = "B"
```

## Enjoy the Game!

Run the script, answer the questions, and see how well you know the quiz topics. Have fun playing!
