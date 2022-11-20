# 6. Write a python program to append elements from another list to the current list.( firstlist = ["Java", "Python", "SQL"] secondlist = ["C", "Cpp", "NoSQL"] )

firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] 
i=0
while (i<3):
    firstlist.append(secondlist[i])
    i+=1
print(firstlist)