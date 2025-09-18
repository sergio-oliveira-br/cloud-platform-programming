# week_1/recommended_weight/calculator.py
from week_1.recommended_weight.user_age import UserAge
from week_1.recommended_weight.user_height import UserHeight


# Problem 2: Write an application that displays the
# recommended weight given the user’s age and height
# (in centimeters) using the following formula:
# RW = (height - 100 + age % 10) * 0.90

class Calculator:

    @staticmethod
    def weight_calculator(age, height):
        """Calculates the recommended weight based on age and height."""
        recommended_weight = (height - 100 + age % 10) * 0.90
        return recommended_weight