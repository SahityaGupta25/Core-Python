'''
8. Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement
'''
x=input("Enter a String\t")
y=input("Enter a String\t")
print(x)
match (x,y):
    case (x,y) if x==y:
        print("Identical")
    case (x,y) :
        if x>y :
            print(y,x,sep="\n")
        else :
            print(x,y,sep="\n")
      
      