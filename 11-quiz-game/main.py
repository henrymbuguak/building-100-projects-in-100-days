from data_model_question import Question
from data import question_data
from quiz import QuizBrain

def create_question_list():
    """
    Creates a list of Question objects from the question data.

    Returns:
    - list: A list of Question objects.
    """
    question_list = []
    for question in question_data:
        text = question["question"]
        answer = question["correct_answer"]
        question_bank = Question(text, answer)
        question_list.append(question_bank)
    return question_list

def main():
    """
    The main function to run the quiz game.

    Creates a list of questions and initializes the QuizBrain.
    Continuously prompts the user for the next question until there are no more questions.
    Displays the final score at the end.
    """
    questions = create_question_list()
    quiz = QuizBrain(questions)
    while quiz.has_more_questions():
        quiz.next_question()
    quiz.show_score()

if __name__ == "__main__":
    main()
