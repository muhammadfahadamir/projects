status = [True, False, True, False] 
newlist = []

for x in status:
  if x==True:
    newlist.append(x)

print(len(newlist))

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist1 = [x for x in fruits if "a" in x]

print(newlist1)