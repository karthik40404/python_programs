# Person (Base Class)
# Employee (Derived from Person) - Single Inheritance
# Manager (Derived from Employee) - Multilevel Inheritance
# DepartmentHead (Derived from Manager and Employee) - Multiple Inheritance
# HRManager (Derived from DepartmentHead) - Hierarchical Inheritance

class person():
    def __init__(self) -> None:
        print('register')

class employee(person):
    def log(self):
        print('login')

class manager(employee):
    def add(self):
        print('add employee')

class departmenthead(manager,employee):
    def monitor(self):
        print('monitoring')

class hr_manger(departmenthead):
    def manage(self):
        print('managing')