import random


def generate_random_integer(minimum_no, maximum_no):
    """
    Generating Random integer between min and max with end points included.
    """
    return random.randint(minimum_no, maximum_no)


def generate_random_operator():
    ''' 
    Generating random arithmetic operator '+','-','*'
    '''
    return random.choice(['+', '-', '*'])


def performance(num1, num2, operator):
    ''' Perform the arithmetic operation between 'n1' and 'n2' according to the chosen operator 'operator'
    '''
    p = f"{num1} {operator} {num2}"

    if operator == '+': 
        result = num1 + num2
    elif operator == '-': 
        result = num1 - num2
    else: 
        result = num1 * num2
    return p, result


# Present the user a set of questions  and return the result
def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

 # Iterate over total number of questions

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, correct_answer = performance(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()