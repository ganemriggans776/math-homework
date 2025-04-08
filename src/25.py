def calculate_area(shape):
    """
    Calculate the area of a shape.
    Args:
        shape (str): The type of shape ('rectangle', 'circle', 'triangle').
    
    Returns:
        float: The area of the shape.
    """
    if shape == "rectangle":
        length = 10
        width = 5
        return length * width
    elif shape == "circle":
        radius = 7
        return 3.1415 * (radius ** 2)
    elif shape == "triangle":
        base = 8
        height = 6
        return 0.5 * base * height
    else:
        raise ValueError("Unsupported shape")

# Example usage
area_rectangle = calculate_area("rectangle")
area_circle = calculate_area("circle")
area_triangle = calculate_area("triangle")
