# week_1/recommended_weight/main.py

from week_1.recommended_weight.introduction import Introduction
from week_1.greeting.greetings import Greeting
from week_1.recommended_weight.user_age import UserAge
from week_1.recommended_weight.user_height import UserHeight
from week_1.recommended_weight.calculator import Calculator

# Problem 2: Write an application that displays the
# recommended weight given the user’s age and height
# (in centimeters) using the following formula:
# RW = (height - 100 + age % 10) * 0.90

def main():

    # Introduction
    print(Introduction().intro())
    username = input('Please enter your name: \n')
    welcome = Greeting(username)
    print(welcome.greet())

    # Age
    user_age = input('Lets start with your age, how old are you? ')
    age = int(UserAge.get_user_age(user_age))
    print(age)

    # Height
    user_height = input('\nNow, what is your current height in cm?')
    height = int(UserHeight.get_user_height(user_height))
    print(height)

    # Calculator
    recommended_w = Calculator.weight_calculator(age, height)

    print("The recommend height is: " + str(recommended_w)+ "kg")

if __name__ == "__main__":
  main()