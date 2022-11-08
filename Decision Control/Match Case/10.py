'''
10. Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday
'''
x=input("Enter Your Favourite Colour\t")
print(x)
match x:
    case x if ("yellow") in x :
        print("Monday")
    case x if ("blue") in x  :
        print("Tuesday")
    case x if ("orange") in x   :
        print("Wednesday")
    case x if ("white") in x  :
        print("Thursday")
    case x if ("black") in x  :
        print("Friday")
    case x if ("red") in x  :
        print("Saturday")
    case _:
        print("Sunday")