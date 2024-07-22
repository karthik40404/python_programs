from add import *
from sub import *
from mul import *
from div import *
data = []
print("1. Add \n2. sub \n3. multi \n4. div ")
while True:
    a=int(input("enter a number :"))
    b=int(input("enter a number :"))

    ch = int(input("Enter your choice: "))
    if ch == 1:
        addition(data)
    elif ch == 2:
        substration(data)
    elif ch == 3:
        multiplication(data)
    elif ch == 4:
        division(data)
    elif ch == 5:
         break