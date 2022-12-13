# Accessing Each Element of a Container using While Loop.Without Getting an Error.

t1=(16, 25, 2, 9, 66, 29)
it=iter(t1)
while True:
    try:
        print(next(it),end=' ')
    except StopIteration:
        break
print(type(it))


