## Singleton Pattern Implementation in Python using class decorator

def singleton(cls):
    _instances = {}

    def wrapper(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    return wrapper

@singleton
class Logger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)
        print(f"Log: {message}")

logger1 = Logger()
logger1.log("This is the first log message.")
logger2 = Logger()
logger2.log("This is the second log message.")
print(logger1 is logger2)