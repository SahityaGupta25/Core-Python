# 1. Write a Python script to create a list of first N natural numbers.

n=int(input("Enter value of 'n'\t"))
i=1
l1=[]
while (i<=n):
    l1.append(i)
    i+=1
print(l1)