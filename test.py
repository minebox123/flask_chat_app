def decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


@decorator
def say_hello():
    print("hello")


@decorator
def say_something(text):
    print(text)
    return "HI Guys"


say_hello()
say = say_something("good day")
