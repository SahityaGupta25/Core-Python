# 10. Write a python script to display all prime numbers within a range.
# range
#start = 15
#end = 45
 
for y in range(15,46) :
    if y>1:
        for z in range(2,y) :
            if (y%z)==0:
                break
        else :
            print(y,end=' ')    
    