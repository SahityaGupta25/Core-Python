# FILTER
# List of Vowels
l1=['a','e','i','o','u']
r1=['s','h','t','e','t','i','a','q','y']

def test(variable):
    if (variable in l1):
        return True
    else:
        return False

x=list(filter(test,r1))
print(x)
