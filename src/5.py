def get_random_number(min_value, max_value):
    return randint(min_value, max_value)

def get_random_math_operation(operations=["+", "-", "*", "/"]):
    return choice(operations)

def solve_math_equation(eq):
    eq = eq.replace("x", str(get_random_number(1, 10)))
    op = get_random_math_operation()
    if op == "+":
        return int(eval(eq)) + get_random_number(1, 10)
    elif op == "-":
        return int(eval(eq)) - get_random_number(1, 10)
    elif op == "*":
        return int(eval(eq)) * get_random_number(1, 10)
    else:
        return int(eval(eq)) / get_random_number(1, 10)

def main():
    eq = input("Enter a math equation: ")
    if "x" in eq:
        print(solve_math_equation(eq))
    else:
        print("Invalid equation")

main()
