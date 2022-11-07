# 12. Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part

x=complex(input("Enter a Complex Number\t"))
'''
if (x.imag>x.real):
    print("Imaginary is Greater")
else :
    print("Real part is Greater")
'''
y= ("Real part is Greater" if x.real>x.imag else "Imaginary part is Greater")
print(y)