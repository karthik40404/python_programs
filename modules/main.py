from reg import *
from tab import *
data=[]
while True:
    print("1. Add \n2. View \n3. Update \n4. Delete \n5. Exit")
    ch=int(input("enter ur choice :"))
    if ch==1:
        print(register(data))
    elif ch==2:
        table(data)