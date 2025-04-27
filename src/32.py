def square_root(num):
    if num < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    
    result = num ** 0.5
    return round(result)
