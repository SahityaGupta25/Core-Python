# 1. Write a python script to calculate sum of first N natural numbers


x=int(input("Enter a Number\t"))
z=0
for y in range(x+1) :
    z=y+z
print("The Sum of",x,"Numbers is=",z)