def square_root(num):
    if num < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return num ** 0.5

try:
    result = square_root(9)
except ValueError as e:
    print(e)

result = square_root(-4)  # This will raise an error
