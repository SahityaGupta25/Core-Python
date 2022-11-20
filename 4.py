# 4. Write a Python script to find the greatest number in a given list of numbers.

a=int(input("Enter Length of List ofNumbers\t"))
i=1
l1=[]
while (i<=a):
    l1.append(int(input("Enter Value")))
    i+=1
print("The Greatest No. in the list is =",max(l1))
