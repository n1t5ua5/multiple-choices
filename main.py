class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions = [
    Question(
        "1. Which of the following is a solution to the equation c + (4 – 3c) – 2 = 0?\n"
        "A. -1\n"
        "B. 0\n"
        "C. 1\n"
        "D. 2\n",
        "C"
    ),
    Question(
        "3. Which of the following is a solution to the equation x^2 – 6x + 5 = 0?\n"
        "A. x = -5\n"
        "B. x = -1\n"
        "C. x = 1\n"
        "D. x = 5\n",
        "D"
    ),
    Question(
        "6. Factor completely: x^2 – x – 6?\n"
        "A. (x – 2)(x + 3)\n"
        "B. (x – 1)(x – 6)\n"
        "C. (x + 2)(x – 3)\n"
        "D. (x + 1)(x – 6)\n",
        "C"
    ),
    Question(
        "8. Which of the following is equivalent to the expression (3ab)(-5ab)?\n"
        "A. -2ab\n"
        "B. -2a^2b^2\n"
        "C. -15ab\n"
        "D. -15a^2b^2\n",
        "B"
    ),
    Question(
        "10. Which of the following is the equation of a line that passes through (-2, -1) and (-4, -3)?\n"
        "A. y = x + 1\n"
        "B. y = x + 1\n"
        "C. y = x – 1\n"
        "D. y = x – 1\n",
        "A"
    ),
]


def run_quiz(questions):
    score = 0
    exit_commands = ['exit', 'quit', 'q']

    for question in questions:
        answer = input(question.prompt)
        if answer.lower() in exit_commands:
            print("So long for now!")
            return
        if answer.upper() == question.answer:
            score += 1
    print(f"You got {score}/{len(questions)} correct.")


run_quiz(questions)
