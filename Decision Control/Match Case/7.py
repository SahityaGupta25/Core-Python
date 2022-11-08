'''
7. Write a python program to check whether a given number is positive, negative or
zero using match case statement
'''
x=int(input("Enter a Number\t"))
print(x)
match x:
    case x :
        if x==0:
            print("Zero '0'")
        elif x<0 :
            print("Negative '-ve' ")
        else :
            print("Positive '+ve' ")