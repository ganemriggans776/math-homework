 import random
 
def get_random_code():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    operators = ["+", "-", "*", "/"]
    
    code = ""
    
    for i in range(5):
        num1 = random.choice(numbers)
        num2 = random.choice(numbers)
        operator = random.choice(operators)
        
        if operator == "+":
            code += f"{num1} + {num2}"
        elif operator == "-":
            code += f"{num1} - {num2}"
        elif operator == "*":
            code += f"{num1} * {num2}"
        else:
            code += f"{num1} / {num2}"
            
    return code