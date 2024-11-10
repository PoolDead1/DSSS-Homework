import random


def random_number_generator(min_value, max_value):
    """
    This function generates a random number between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def random_operator_generator():
    """
    This function generates a random operator.
    """
    
    return random.choice(['+', '-', '*'])


def arithmetic_problem_and_answer_generator(number_1, number_2, operator):
    """
    This function generates a random math problem and its solution.
    Parameters:
    - number_1: The first number
    - number_2: The second number
    - operator: The arithmetic operator(+, -, *)

    Return:
    problem: A string representing the arithmetic problem
    answer: The correct answer to the arithmetic problem
    """
    problem = f"{number_1} {operator} {number_2}"
    if operator == '+':
        answer = number_1 + number_2
    elif operator == '-':
        answer = number_1 - number_2
    else: # operator = "*"
        answer = number_1 * number_2
    return problem, answer

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number_1 = random_number_generator(1, 10)
        number_2 = random_number_generator(1, 5)
        operator = random_operator_generator()

        PROBLEM, ANSWER = arithmetic_problem_and_answer_generator(number_1, number_2, operator)
        print(f"\nQuestion: {PROBLEM}")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == ANSWER:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")
        except ValueError:
            print("Invalid Input! Please enter an integer.")            

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
