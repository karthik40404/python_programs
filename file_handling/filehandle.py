# t=open('python_programs/file_handling/new1.txt','w')
# t.write('124k'+'lkjhgfd')

t=open('python_programs/file_handling/new2.txt','w')
a=int(input("enter the limit :"))
for i in range(a):
    b=input("enter the name :")
    t.write(b+"\n")

