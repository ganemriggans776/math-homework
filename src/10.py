import random

def get_random_math_problem(max_value=100):
    """
    Generates a random math problem with two integers and a operator (+, -, x, /).

    Args:
        max_value (int, optional): The maximum value for the numbers in the problem. Defaults to 100.

    Returns:
        tuple(int, int, str): A tuple containing three elements: two integers and a operator.
    """
    num1 = random.randint(1, max_value)
    num2 = random.randint(1, max_value)
    op = random.choice(["+", "-", "*", "/"])
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    else:
        result = num1 / num2
    return (num1, num2, op, result)

get_random_math_problem()