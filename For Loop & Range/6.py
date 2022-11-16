# 6. Write a python script to print first N even natural numbers.

x=int(input("Enter a Number\t"))
for y in range(2,x*2+1,2) :
    print(y,end=' ')