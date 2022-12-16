# REDUCE

import functools
l1=[1,2,3,4]
def mul(a,b):
    return a*b
r=functools.reduce(mul,l1)
print(r)
