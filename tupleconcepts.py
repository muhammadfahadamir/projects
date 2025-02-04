fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, *yellow, red) = fruits2

print(green)
print(yellow)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  
for i in range(len(thistuple)):
  print(thistuple[i])
  
  
j = 0
while j < len(thistuple):
  print(thistuple[j])
  j = j + 1


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)