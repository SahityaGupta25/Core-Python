# 4. Write a python script to calculate sum of first N odd natural numbers

x=int(input("Enter a Number\t"))
sum=0
for y in range(1,x*2+1,2) :
    sum+=y
print(sum)