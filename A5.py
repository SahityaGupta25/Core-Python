'''
Write a Program to ask user to enter a even no. three times .If user fails to enter a even number all 3 times announce him a loser . If user entered a even no then no more chances will be given to him or her announce he/she winner. 
'''
i=1
while (i<=3):
    n=int(input("Enter a Number\t"))
    if (n%2==0):
        break
    i+=1
if (i==4):
    print("'Loser'")
else :
    print("'Winner'")    
