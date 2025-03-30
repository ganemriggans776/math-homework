def square_root(number):
    if number > 0:
        return number ** 0.5
    else:
        raise ValueError("Number should be greater than 0")

try:
    print(square_root(-1))
except ValueError as e:
    print(e)
