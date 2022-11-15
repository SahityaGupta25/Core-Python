# Take Input if 'r' appears in that string so stop printing. If not then print "All Characters are Processed" using 'For Loop'.

x=input("Enter a String\t")
for y in x:
    if y=='r':
        break
    print(y,end=' ')
else :
    print("All Characters are Processed")