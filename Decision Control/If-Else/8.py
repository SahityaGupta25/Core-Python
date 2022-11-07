'''
8. Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots
'''
a=int(input("Enter a '''a'''\t"))
b=int(input("Enter a '''b'''\t"))
c=int(input("Enter a '''c'''\t"))
d=b**2-4*a*c
if (d>0):
    print("two real & distinct roots")
elif (d==0):
    print("real & equal roots")
else :
    print("Imaginary Roots")