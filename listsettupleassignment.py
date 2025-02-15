numbers=list(range(1,21))
print(numbers)
squares=[]
for x in numbers:
    if x%2==0:
        squares.append(x*x)
print(squares)
evens=[]
for x in numbers:
    if x%3==0:
        evens.append(x)
print(evens)
numbers.sort(reverse = True)
print(numbers)
numbers2=[]
for x in numbers:
    if x>15:
        numbers2.append(x)
print(numbers2)
numbers.insert(1,25)
print(numbers)
list=[21, 22, 23] 
numbers.extend(list)
print(numbers)