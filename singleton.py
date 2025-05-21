"""
This is an example of the singleton creational pattern implemented in Python.

We have a Logger class that ensures only one instance of the logger exists
throughout the application.
"""


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message):
        print(f"Log: {message}")


logger1 = Logger()
logger2 = Logger()

logger1.log("This is a log message from logger1.")
logger2.log("This is a log message from logger2.")

print("logger1 and logger2 are the same instance?", logger1 is logger2)
