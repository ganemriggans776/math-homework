import random
def random_math_problem(numbers=()):
    numbers = []
    operators = ["+", "-", "*"]
    # generate 2 random numbers between 1 and 10
    for i in range(2):
        numbers.append(random.randint(1, 10))
    # choose a random operator
    operator = random.choice(operators)
    problem = "{} {} {}".format(numbers[0], operator, numbers[1])
    return problem