'''
10. Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same.
'''

a=int(input("Enter a '''a'''\t"))
b=int(input("Enter a '''b'''\t"))
c=int(input("Enter a '''c'''\t"))
'''
if (a>b) and (a>c):
    print("'1st' Number is Greater")
elif (b>c) and (b>a):
    print("'2nd' Number is Greater")
else :
    print("'3rd' Number is Greater")
'''
x=((a if a>c else c)if a>b else (b if b>c else c) )
print(x)

