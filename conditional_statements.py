age=int(input("enter age"))
if age>=18:
    print("yes")
else:
    print("no")    

experiance=int(input("enter the years of work you have done :"))
salary=int(input("enter the salary :"))
if experiance>=5:
    print("yes,give 5% raise")
    print(salary*0.05+salary)
else:
    print("no")        