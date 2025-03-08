
def get_random_math_expression(variables=['x', 'y', 'z']):
    """
    Generates a random math expression using the given variables.
    """
    import random
    operators = ['+', '-', '*', '/', '**']
    operator = random.choice(operators)
    if operator == '+':
        return f'{random.randint(1, 10)} + {random.randint(1, 10)}'
    elif operator == '-':
        return f'{random.randint(1, 10)} - {random.randint(1, 10)}'
    elif operator == '*':
        return f'{random.randint(1, 10)} * {random.randint(1, 10)}'
    elif operator == '/':
        return f'{random.randint(1, 10)} / {random.randint(2, 5)}'
    else:
        return f'{random.randint(1, 10)} ** {random.randint(2, 5)}'
