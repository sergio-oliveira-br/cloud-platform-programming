# main.py

from week_1.greeting.greetings import Greeting

# Problem 1: Develop an application that asks the user
# for her/his name, and then greets them with their
# name.

def main():
    user_name = input('What is your name? ')
    greeting = Greeting(user_name)
    print(greeting.greet())


if __name__ == "__main__":
  main()