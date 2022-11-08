# 2. Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division

a=("Press '1' for Addition")
b=("Press '2' for Substraction")
c=("Press '3' for Multiplication")
d=("Press '4' for Division")
print(a,b,c,d,sep="\n")
match=int(input("Choose Your Operation\t"))
print(match)

match (match):
    case 1:
        print("Enter Value for Addition")
        x=int(input("Enter a 1st Number\t"))
        y=int(input("Enter a 2nd Number\t"))
        a_1=x+y
        print(a_1)
    case 2:
        print("Enter Value for Substraction")
        x=int(input("Enter a 1st Number\t"))
        y=int(input("Enter a 2nd Number\t"))
        a_1=x-y
        print(a_1)
    case 3:
        print("Enter Value for Multilpication")
        x=int(input("Enter a 1st Number\t"))
        y=int(input("Enter a 2nd Number\t"))
        a_1=x*y
        print(a_1)
    case 4:
        print("Enter Value for Division")
        x=int(input("Enter a 1st Number\t"))
        y=int(input("Enter a 2nd Number\t"))
        a_1=x//y
        print(a_1)
    case _:
        print("Invalid Value")
    
    
    