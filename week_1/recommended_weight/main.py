# week_1/recommended_weight/main.py

import greetings
import calculator

# Problem 2: Write an application that displays the
# recommended weight given the user’s age and height
# (in centimeters) using the following formula:
# RW = (height - 100 + age % 10) * 0.90

def main():

    # Introduction
    print("*** Lab1. This is the weight calculator. ***\n")

    # Greeting
    username = input('Please enter your name: \n')
    print(greetings.say_hi(username))

    # Age
    age = int(input('Lets start with your age, how old are you? '))
    print(age)

    # Height
    height = int(input('\nNow, what is your current height in cm?'))
    print(height)

    # Calculator
    recommended_w = calculator.weight_calculator(age, height)

    print("The recommend height is: " + str(recommended_w)+ "kg")

if __name__ == "__main__":
  main()