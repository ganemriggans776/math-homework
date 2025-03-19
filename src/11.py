def get_random_code():
    # Generate a random number between 1 and 100
    num = randint(1, 100)
    # Generate a random operation (+, -, *, /)
    op = choice(['+', '-', '*', '/'])
    # Generate two random numbers to perform the operation on
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    # Evaluate the expression
    result = eval(f"{num1} {op} {num2}")
    # Return the code as a string
    return f"{num1} {op} {num2} = {result}"
