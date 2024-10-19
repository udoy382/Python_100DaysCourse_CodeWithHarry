# Decorators in Python


def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning!")
        fx(*args, **kwargs)
        print("Thanks for using this functions")
    return mfx


@greet
def hello():
    print("Hello World!")

@greet
def add(a, b):
    print(a + b)


hello()
# greet(hello())


add(3, 4)