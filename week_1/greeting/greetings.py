# greetings.py

class Greeting:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return 'Hello, {}!' .format(self.name)