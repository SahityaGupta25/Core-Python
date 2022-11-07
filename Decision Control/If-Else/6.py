# 6. Write a python script to check whether a given number is a three digit number or not.

x=int(input("Enter a Number\t"))
y=("Three Digit Number" if 99<x<1000 else "Not Three Digit")
print(y)