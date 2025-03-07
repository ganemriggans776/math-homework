import random

def get_random_math_expression(variables):
    operators = ["+", "-", "*", "/"]
    expression = ""
    for i in range(random.randint(2, 4)):
        operand1 = random.choice(variables)
        operand2 = random.choice(variables)
        operator = random.choice(operators)
        expression += f"{operand1} {operator} {operand2}"
    return expression