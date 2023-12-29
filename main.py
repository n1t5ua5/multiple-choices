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
        "2. Graph the solution of y – 2 > 1 on a number line.\n"
        "A.\n"
        "B.\n"
        "C.\n"
        "D.\n",
        "Explanation: To solve y – 2 > 1, we get y > 3. The graph on a number line would show all values greater than 3. However, since a number line cannot be displayed here, just mark a ray pointing to the right from the point y = 3."
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
        "4. What is the value of the algebraic expression if x = 7, y = -1, and z = 2?\n"
        "6x(y^2z)\n"
        "A. -12\n"
        "B. -6\n"
        "C. 1\n"
        "D. 6\n",
        "Explanation: Substitute the given values into the expression: 6x(y^2z) = 6 * 7 * (-1)^2 * 2 = 6 * 7 * 1 * 2 = 84. Therefore, the value is not explicitly given as an option."
    ),
    Question(
        "5. Which of the following is equivalent to (8 – 5) ÷ 2 * 3 ?\n"
        "A.\n"
        "B.\n"
        "C.\n"
        "D.\n",
        "Explanation: (8 – 5) ÷ 2 * 3 = 3 ÷ 2 * 3 = 1.5 * 3 = 4.5. Therefore, the result is not explicitly given as an option."
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
        "7. Simplify the following expression: 3x^4 / y^2 * xy^2\n"
        "A.\n"
        "B.\n"
        "C.\n"
        "D.\n",
        "Explanation: Simplify the expression: 3x^4 / y^2 * xy^2 = 3x^3 / y^4. Therefore, the result is not explicitly given as an option."
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
        "9. What percent of the grid is shaded?\n"
        "A. 35%\n"
        "B. 40%\n"
        "C. 45%\n"
        "D. 55%\n",
        "Explanation: The shaded part consists of 5 squares out of a total of 9 squares. Therefore, the percent shaded is approximately 55.56%, which is closest to option D, 55%."
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
