from collections import Counter

X = int(input())  
shoe_sizes = list(input().split())  

shoe_inventory = Counter()
for size in shoe_sizes:
    shoe_inventory[int(size)] += 1

N = int(input())  
earnings = 0  

for _ in range(N):
    customer_input = input().split()  
    size = int(customer_input[0])  
    price = int(customer_input[1])  
    if shoe_inventory[size] > 0:  
        earnings += price  
        shoe_inventory[size] -= 1  

print(earnings)  



#2nd from collections import Counter

X = int(input())  
shoe_inventory = Counter(input().split())  

N = int(input())  
earnings = 0  

for _ in range(N):
    size, price = input().split()  
    if shoe_inventory[size] > 0:  
        earnings += int(price)  
        shoe_inventory[size] -= 1  

print(earnings)