# for functions without parametres
def greet(fx):
    def wrapper():
        print("before using the function...")
        fx()
        print("function excecuted. Thanks for using this function.")
    return wrapper


@greet  # ignore ()
def hello():
    print("HELLO")


hello()

# for function with parametress


def good(dx):
    def wrap(*args, **kwargs):
        print("before ")
        dx(*args, **kwargs)
        print("after ")
    return wrap


@good
def sum(a, b):
    print("the sum is", a+b)


sum(3, 5)
