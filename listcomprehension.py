status = [True, False, True, False] 
newlist = []

for x in status:
  if x==True:
    newlist.append(x)

print(len(newlist))

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist1 = [x for x in fruits if "a" in x]

print(newlist1)

newlist1 = [x for x in fruits if x != "apple"]

newlist2 = [x for x in fruits]

newlist3 = [x for x in range(len(fruits))]

newlist4 = [x for x in range(10) if x%2==0]

newlist5 = [x.upper() for x in fruits]

newlist6 = [x+5 for x in range(10)]

newlist7 = ['hello' for x in fruits]

newlist8 = [x if x != "banana" else "orange" for x in fruits]