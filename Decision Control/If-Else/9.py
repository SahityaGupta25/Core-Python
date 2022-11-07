'''
9. Write a python script to check whether a given year is a leap year or not.
'''

x=int(input("Enter a Value of Year\t"))
if (x%100==0) and (x%4==0):
    print("Leap Year")
elif (x%4==0) :
    print("Leap year")
elif (x%100==0) and (x%4!=0):
    print("Not Leap year")
else :
    print("Not a Leap Year")