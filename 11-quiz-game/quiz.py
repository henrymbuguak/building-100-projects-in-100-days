class QuizBrain:
    """
    A class to manage the quiz game.

    Attributes:
    - question_number (int): The current question number.
    - question_list (list): A list of Question objects.
    - score (int): The current score of the user.

    Methods:
    - next_question(): Retrieves the next question and prompts the user for an answer.
    - has_more_questions(): Checks if there are more questions left.
    - check_answer(user_answer, correct_answer): Checks the user's answer and updates the score.
    - show_score(): Displays the final score.
    """

    def __init__(self, question_list) -> None:
        """
        Initializes the QuizBrain with a list of questions.

        Args:
        - question_list (list): A list of Question objects.
        """
        self.question_number = -1
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """
        Retrieves the next question and prompts the user for an answer.

        Increments the question number and prints the current question.
        If there are no more questions, calls show_score().
        """
        self.question_number += 1
        if self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]
            user_answer = input(f"Q{self.question_number + 1}: {current_question.text} (True/False): ")
            self.check_answer(user_answer, current_question.answer)
        else:
            self.show_score()
            return None
    
    def has_more_questions(self):
        """
        Checks if there are more questions left.

        Returns:
        - bool: True if there are more questions, False otherwise.
        """
        return self.question_number + 1 < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """
        Checks the user's answer and updates the score.

        Args:
        - user_answer (str): The user's answer.
        - correct_answer (str): The correct answer.
        """
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number + 1}\n")
    
    def show_score(self):
        """
        Displays the final score.
        """
        print("No more questions.")
        print(f"Your final score is: {self.score}/{len(self.question_list)}")
