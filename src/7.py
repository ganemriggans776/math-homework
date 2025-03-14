import random
def get_random_math_problem():
    # Generate two random numbers
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    # Choose a random operation (+, -, *, /)
    op = random.choice(["+", "-", "*", "/"])
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    else:
        return num1 / num2

print(get_random_math_problem())