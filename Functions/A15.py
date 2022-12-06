# Variable Length Argument ( List )
def avg(*l):
    x=sum(l)//len(l)
    return x

print(avg(10,20,30,40,50,60))