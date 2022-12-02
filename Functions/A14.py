# Variable Length Argument

# Average of 2 Numbers

def avg(*t):
    x=sum(t)//len(t)
    return x

print(avg(10,20,30,40,50,60))
