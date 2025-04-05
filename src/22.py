def calculate_average(numbers):
    if not numbers:  # Check if the list of numbers is empty
        return None
    else:
        average = sum(numbers) / len(numbers)
        return average

numbers = [10, 20, 30, 40, 50]  # Example numbers
average = calculate_average(numbers)
print("Average:", average)
