'''
3. Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isoscelestriangle or not
b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.
'''
a=("Press '1' for Isosceles Triangle")
b=("Press '2' for Right Angled Triangle")
c=("Press '3' for Equilateral Triangle")
print(a,b,c,sep="\n")
sides=int(input("Choose Your Operation\t"))
print(sides)
match sides:
    case 1:
        x=int(input("Enter a 1st Number\t"))
        y=int(input("Enter a 2nd Number\t"))
        z=int(input("Enter a 3rd Number\t"))
        if x==y or y==z or z==x:
            print("Isoscelestriangle")
        else :
            print("Not An Isoscelestriangle")
    case 2:
        x=int(input("Enter a 1st Number\t"))
        y=int(input("Enter a 2nd Number\t"))
        z=int(input("Enter a 3rd Number\t"))
        if x**2+y**2==z**2:
            print("Right Angled Triangle")
        else :
            print("Not a Right Angled Triangle")
    case 3:
        x=int(input("Enter a 1st Number\t"))
        y=int(input("Enter a 2nd Number\t"))
        z=int(input("Enter a 3rd Number\t"))
        if x==y and y==z :
            print("Equilateral Triangle")
        else :
            print("Not An Equilateral Triangle")
    case _:
        print("Invalid Value")   
