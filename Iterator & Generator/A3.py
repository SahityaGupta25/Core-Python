# Accessing Each Element of a Container using While Loop.Without Getting an Error.

t1=(16, 25, 2, 9, 66, 29)
it=iter(t1)
i=1
while i<=6:
    print(next(it),end=' ')
    i+=1
    
print(type(it))