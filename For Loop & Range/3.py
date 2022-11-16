# 3. Write a python script to calculate sum of cubes of first N natural numbers

x=int(input("Enter a Number\t"))
sum=0
for y in range(x+1) :
    sq=y**3
    sum=sum+sq
print(sum)