'''
9. Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year
'''
x=int(input("Enter a Year\t"))
print(x)
match x:
    case x if x%4==0 and x%100!=0 :
        print("Non century leap year")
    case x if x%400==0 :
        print("Century leap year")
    case x if x%4!=0 and x%100!=0 :
        print("Non century non leap year")
    case x if x%4!=0 and x%100==0 :
        print("Century non leap year")
    case _:
        print("Not a Leap Year")