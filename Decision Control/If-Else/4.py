# 4. Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.

x=int(input("Enter a Number\t"))
y=int(input("Enter a Number\t"))
if  (x==y):
    print("x is =",x,"y is =",y)
elif (x>y):
    print("x is Greater than y")
else :
    print("y is Greater")
