class Power:
    def __init__(self, arg):
        self.power = arg

    def __call__(self, func):
        def wrap(a, b):
            return func(a, b) ** self.power
        return wrap


@Power(2)
def foo(a, b):
    return a*b


print(foo(2, 5))
