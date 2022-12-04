# 1. Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.

def lt(l):
    l1=[]
    for x in l:
        if x not in l1:
            l1.append(x)
    return l1

print(lt([True,6,7.8,False,(4+5j),True,6]))