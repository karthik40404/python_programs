# l=[1,2,"welcome",1,3]
# print(l[2])

# l=[1,2,"welcome",1,3]
# if 2 in l:
#     print("is there")
# else:
#     print("is not there")    

# l=[1,2,"welcome",1,3]
# for i in l:
#     print(i)    
# print(type(l))
# print(len(l))

# l=[1,2,"welcome",1,3]
# l[2]="hello"
# print(l)


# l=[1,2,"welcome",1,3]
# del l[4]
# print(l)

'''list methods'''


# L=[]
# L.append(20)
# L.append(24)
# print(L)



# L=[]
# L.append(20)
# L.append(24)
# L.insert(1,50)
# L.insert(4,[29,48,5])
# print(L)



# L=[]
# L.append(20)
# L.append(24)
# L.insert(1,50)
# L.insert(4,[29,48,5])
# L.extend([100,200,50])
# print(L)


# L=[]
# L.append(20)
# L.append(24)
# L.append(246)
# L.append(55)
# L.insert(1,50)
# L.insert(4,[29,48,5])
# L.extend([100,200,50])
# L.remove(20)
# L.remove([29,48,5])
# print(L)


# name=[]
# a=int(input("enter the limit :"))
# for i in range(a):
#     b=str(input("enter the name"))
#     name.append(b)
#     print(name)



# name=[]
# while True:
#     print('1.add\n2.display\n3.update\n4.delete\n5.exit')
#     choice=int(input("enter your choice :"))
#     if choice==1:
#         limit=int(input('enter the limit :'))
#         for i in range(limit):
#             b=str(input("enter a names :"))
#             name.append(b)
#     elif choice==2:
#         for i in name:
#             print(i)
#     elif choice==3:
#         old_name=input('enter name to update :')
#         if old_name in name:
#             new_name=input('new_name :')
#             pos=name.index(old_name) 
#             name[pos]=new_name
#     elif choice==4:
#         old_name=input('enter name:')
#         if old_name in name:
#             name.remove(old_name)            
