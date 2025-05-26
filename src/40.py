import math

def calculate_area_of_triangle(base, height):
    """
    Calculate the area of a triangle using Heron's formula.
    
    Parameters:
        base (float): The length of the base of the triangle.
        height (float): The height of the triangle above the base.
        
    Returns:
        float: The area of the triangle.
    """
    s = (base + height) / 2
    area = math.sqrt(s * (s - base) * (s - height))
    return area

# Example usage
base = 4.0
height = 3.0
print("Area of the triangle:", calculate_area_of_triangle(base, height))
