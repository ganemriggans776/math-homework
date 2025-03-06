import math
def get_random_number(min_value, max_value):
    return math.floor((max_value - min_value + 1) * random.random() + min_value)