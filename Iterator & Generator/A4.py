def f1():
    yield 66
    print("*")
    yield 25
    print("**")
    yield 29
    print("***")

x=f1()
print(next(x))
print(next(x))
print(next(x))

