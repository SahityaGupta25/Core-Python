
x=[1, 2, 3, 4, 5, 6, 7, 8]
for y in x:
    if y==4:
        del x[3]
print(x,end=' ')