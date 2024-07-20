# OOP Quiz Game

Welcome to the OOP Quiz Game! This project is a simple console-based quiz game that utilizes object-oriented programming (OOP) principles to manage the quiz questions and user interactions.

## Introduction

This project demonstrates how to build a quiz game using Python's object-oriented programming features. The game will ask a series of questions, track the user's score, and provide feedback on their answers. The game will continue until all questions have been asked, and then it will display the user's final score.

## Prerequisites

- [Python 3.12](https://www.python.org/downloads/) installed on your system.

## Program Description

The program consists of several components:

- **Question Class**: Represents a single quiz question.
- **QuizBrain Class**: Manages the quiz, including asking questions, checking answers, and tracking the score.
- **Main Script**: Sets up the quiz questions and starts the game.

## How the Code Works

- **Question Class**: This class stores the text and answer for a single quiz question.
- **QuizBrain Class**: This class handles the logic of the quiz. It asks questions, checks if the user's answers are correct, and keeps track of the score.
- **Main Script**: The main script initializes the quiz questions, creates an instance of the QuizBrain class, and starts the quiz loop.

## How to Run the Code

Follow these steps to run the Quiz Game Program:

1. Open your terminal or command prompt.
1. Download the code using the following command:

    ```sh
    git clone https://github.com/henrymbuguak/building-100-projects-in-100-days.git
    ```

1. Navigate to the directory `building-100-projects-in-100-days/11-quiz-game` where `main.py` is saved.
1. Run the program by executing the command:

    ```sh
    python main.py
    ```

1. Follow the prompts.

## Example Usage

When you run the program, you will see the following prompt:

```shell
Welcome to the OOP Quiz Game!
Q1: What is the capital of France? (True/False): False
That's wrong.
The correct answer was: Paris.
Your current score is: 0/1

Q2: What is 2+2? (True/False): True
You got it right!
The correct answer was: 4.
Your current score is: 1/2

Q3: Who wrote 'To Kill a Mockingbird'? (True/False): True
You got it right!
The correct answer was: Harper Lee.
Your current score is: 2/3

No more questions.
Your final score is: 2/3

```

Enjoy exploring the power of OOP with this practical project!
