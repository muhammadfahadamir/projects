thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist2 = ["apple", "banana", "cherry"]
mylist2 = list(thislist2)
print(mylist2)


mylist3 = thislist[:]
print(mylist3)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list4 = ["a", "b" , "c"]
list5 = [1, 2, 3]

for x in list5:
  list4.append(x)

print(list4)


list1.extend(list2)
print(list1)