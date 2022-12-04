# 4. Write a python program to create a function that checks whether a passed string is palindrome or not.

def pd():
    x=input("Enter a Word\t")
    y=x[::-1]
    print("Yes, it is a Palindrome" if y==x else "Not a Palindrome")
pd()