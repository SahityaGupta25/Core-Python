# 3. Write a Python script to create a list of first N even natural numbers.

n=int(input("Enter value of 'n'\t"))
l1=[]
for x in range(2,n*2+1,2):
    l1.append(x)
print(l1)