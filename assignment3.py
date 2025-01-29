#1
integer_lists=[1,5,7,9,3]
print(integer_lists)
print(len(integer_lists))
#2
float_lists=[4.5,10.99,23.75,1.2]
print(float_lists)
x=sum(float_lists)
print(x)
#3
status=[True, False, True, False]
if "True" in status:
    print("yes true is prsent")
#4
mixed_data=[45,"apple",3.14,True,"banana"] 
print(mixed_data)
print(type(mixed_data))
#5
numbers = [1,5,7,9,3]
print(numbers[2])
print(numbers[-3])
#6
prices = [4.5, 10.99, 23.75, 1.2]
print(prices[1:2])
#7
mixed_data = [45, "apple", 3.14, True, "banana"]
print(mixed_data[:2])
print(mixed_data[4])
#8
mixed_data = [45, "apple", 3.14, True, "banana"]
print(mixed_data[-4:])
#9
numbers = [1,5,7,9,3]
numbers[1]=99
print(numbers)
#10
prices = [4.5, 10.99, 23.75, 1.2]
prices[1]=12.5
prices[2]=30.0
print(prices)
#11
mixed_data = [45, "apple", 3.14, True, "banana"]
mixed_data[2]=7.8
print(mixed_data)
#12
status = [True, False, True, False]
status.append(True)
print(status)
#13
numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6]
numbers1.extend(numbers2)
print(numbers1)
#14
fruits = ["apple", "banana"]
extra_fruits = ("kiwi", "mango")
fruits.extend(extra_fruits)
print(fruits)
#15
prices= [4.5, 10.99, 23.75, 1.2]
prices.pop(3)
print(prices)
#16
mixed_data = [45, "apple", 3.14, True, "banana"]
mixed_data.append(True)
#17
status = [True, False, True, False]
print(len(status))
#18
mixed_data = [45, "apple", 3.14, True, "banana"]
if "banana" in mixed_data:
    print("Yes, 'banana' is in the list")
#19
numbers = [1, 5, 7, 9, 3]
print(sum(numbers))
#20
numbers = [1, 5, 7, 9, 3]
v=sum(numbers)
if v/2==0:
    print("sum is even")
else:
    print("sum is uneven")