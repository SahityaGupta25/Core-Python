# 2. Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.

def lt():
    l1=[]
    for x in range(1,31):
        y=x**2
        l1.append(y)
    print(l1)

lt()
