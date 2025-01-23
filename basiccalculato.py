print("These are the the types of calculations. What would you like  to perform?")
print("1.addition")
print("2.subtraction")
print("3.multilicatioon")
print("4.division")



typ_cal=float(input("what type of calculation would you like to perform.?enter only number please?"))
x=float(input("enter first number?"))
y=float(input("second first number?"))
if typ_cal == 1:
    print("addition of two entered number is  ",x+y)
if typ_cal == 2:
    print("subtraction of two entered number is ",x-y)
if typ_cal == 3:
    print("multilication of two entered is ",x*y)
if typ_cal == 4:
    print("divition of two entered number is ",x/y)
 

