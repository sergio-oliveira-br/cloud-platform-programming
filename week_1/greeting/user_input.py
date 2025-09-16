# user_input.py

from week_1.greeting.greetings import Greeting

def main():
    user_name = input('What is your name? ')
    greeting = Greeting(user_name)
    print(greeting.greet())


if __name__ == "__main__":
  main()