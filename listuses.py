a = ["apple", "banana", "cherry"]
print(a)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list4 = ["abc", 34, True, 40, "male"]

print(type(list4))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

print(thislist[2])

print(thislist[-3])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")