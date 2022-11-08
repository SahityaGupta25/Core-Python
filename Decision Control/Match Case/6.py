'''
6. Write a python program to check whether a given string is a multiword string or single word string using match case statement
'''
x=input("Enter a Word\t")
print(x)
match x:
    case x :
        if ' ' in x:
            print("Multiword string")
        else :
            print("Single word string")
      
