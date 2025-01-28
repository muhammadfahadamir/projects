thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist1[1:4] = ["blackcurrant", "watermelon"]
print(thislist1)

thislist2 = ["apple", "banana", "cherry"]
thislist2[1:2] = ["blackcurrant", "watermelon"]
print(thislist2)

thislist3 = ["apple", "banana", "cherry"]
thislist3[1:3] = ["watermelon"]
print(thislist3)

thislist.insert(2, "watermelon")
print(thislist)

thislist.append("orange")
print(thislist)

thislist4 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist4.extend(tropical)
print(thislist4)

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist.remove("apple")
print(thislist)

thislist4.pop(4)
print(thislist4)

del thislist[0]
print(thislist)

thislist.clear()
print(thislist)