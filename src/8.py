def get_random_math_problem(max_value=100):
    operand1 = random.randint(1, max_value)
    operand2 = random.randint(1, max_value)
    operator = random.choice(["+", "-", "*", "/"])
    problem = f"{operand1} {operator} {operand2}"
    solution = eval(problem)
    return (problem, solution)
