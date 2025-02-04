#number one
colors=["red","green","blue"]
colors.append("yellow")
colors[0]="black"
colors.remove("green")
colors.insert(2,"purple")
print(colors)
print(len(colors))
#number 2
list1 =[3,7,1]
list2 =[4,8,2]
list3 =list2 + list1
list3.sort(reverse=True)
list4=[]
for x in list3:
     if x>=4:
          list4.append(x)
print(list4)
print(list3)
print(list3.index(7))
#number 3
nums=[21,7,4,9,15,3]
nums2=[]
numb3=[]
nums2=[x for x in nums if x%2!=0]
print(nums2)
numb3=[x*x for x in nums if x%3==0]
print(numb3)