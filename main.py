class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions = [
    Question(
        "Which built-in Python function will return the length of an object?\n"
        "A. float()\n"
        "B. str()\n"
        "C. len()\n"
        "D. int()\n",
        "C"
    ),
    Question(
        "Which built-in JavaScript method merges two or more arrays?\n"
        "A. .split()\n"
        "B. .shift()\n"
        "C. .join()\n"
        "D. .concat()\n",
        "D"
    ),
    Question(
        "How do you say, 'I love plants & animals' in Spanish?\n"
        "A. Me amo las verduras con las frutas\n"
        "B. Me encanta las flores y los animales\n"
        "C. Me encanta el calor y el frio\n"
        "D. Me amo las gatos con carisma\n",
        "B"
    ),
    Question(
        "¿Cómo se dice 'aprender es divertido' en inglés?\n"
        "A. learning is fun\n"
        "B. apprenticing is dynamic\n"
        "C. aprehending is doubtful\n"
        "D. learning is discerning\n",
        "A"
    )
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.upper() == question.answer:
            score += 1
    print(f"You got {score}/{len(questions)} coreect.")


run_quiz(questions)
