"""
write a program to print grade obtained in a test.Take input from the user and print grade.


90 < X = A
80 < X = B
70 < X = C
60 < X = D
50 < X = E
40 < X = F
30 < X = G
"""
x=int(input("Enter a Number\t"))

if x>90 :
    print("Grade 'A'")
elif x>80 :
    print("Grade 'B'")
elif x>70 :
    print("Grade 'C'")
elif x>60 :
    print("Grade 'D'")
elif x>50 :
    print("Grade 'E'")
elif x>40 :
    print("Grade 'F'")
elif x>30 or x>10 :
    print("Grade 'G'")
else :
    print("Fail")

