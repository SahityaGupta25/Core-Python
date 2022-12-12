# 1. Use iter and next method to access all the elements of a given set using while loop


s1={16, 25, 2, 9, 66, 29}
it=iter(s1)
i=1
while i<=6:
    print(next(it),end=' ')
    i+=1