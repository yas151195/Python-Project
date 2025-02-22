# list of question
# store the answers
# randomly pick questions
# ask the questions
# see if they are correct
# Keep track of the score
# tell the user thier score

import random

questions = {
    "What is keyword to use function inpython?": "def",
    "What data type use to define true or false?": "boolean",
    "Comment in Python?": "#",
    "Opps define in pyhon under?": "class",
    "What is the result of 10 // 3 in python?": "3",
    "what is use to define condition?": "if",
    "What is your name?": "Shaheryar",
    "What is your pet name?": "Bella",
    "What is the value of 2**3?": "8",
    "What is lenght in python?": "len()"
}

def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0
    selected_questions = random.sample(questions_list, total_questions)

    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question]
        if user_answer == correct_answer.lower():
            print("Correct Answer!\n")
            score += 1
        else:
            print(f"Wrong Answer. the correct answer is {correct_answer}. \n")
    print(f" Your total Score is : {score}/{total_questions}")
python_trivia_game()

