# week_1/recommended_weight/calculator.py

# Problem 2: Write an application that displays the
# recommended weight given the user’s age and height
# (in centimeters) using the following formula:
# RW = (height - 100 + age % 10) * 0.90

def weight_calculator(age, height):
    """Calculates the recommended weight based on age and height."""

    if age <= 0 or height <= 0:
        raise ValueError("Age and height must be positive numbers. ")

    elif height > 1000:
        raise ValueError("Height must be less than 1000 meters.")

    return (height - 100 + age % 10) * 0.90