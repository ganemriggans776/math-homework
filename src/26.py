import numpy as np

def calculate_area_rectangle(width, height):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    width (float): The width of the rectangle.
    height (float): The height of the rectangle.
    
    Returns:
    float: The area of the rectangle.
    """
    return width * height

def main():
    # Example usage
    width = 10.0  # in meters
    height = 5.0   # in meters
    area = calculate_area_rectangle(width, height)
    print(f"The area of the rectangle is: {area:.2f} square meters")

if __name__ == "__main__":
    main()
