# 2. Write a python script to calculate sum of squares of first N natural numbers


x=int(input("Enter a Number\t"))
sum=0
for y in range(x+1) :
    sq=y**2
    sum=sum+sq
print(sum)