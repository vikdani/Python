class Member:
    def __init__(self,name,age,phone_number,address,salary):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.address = address
        self.salary = salary

    def print_salary(self):
        print("the salary of employee is",self.salary)

class Employee(Member): 
    def __init__(self,name,age,phone_number,address,salary,specilization):
        self.specialization = specilization 
        super().__init__(name,age,phone_number,address,salary)
        
class Manager(Member):
    def __init__(self,name,age,phone_number,address,salary,department):
        self.department = department
        super().__init__(name,age,phone_number,address,salary)

   
objemp = Employee('botu',22,32424424,'indore',40000,'hr')
    
objmanager = Manager('gullu',24,3232432444,'ujjain',50000,'sales')

print("Employee Details:")
print("Name:", objemp.name)
print("Age:", objemp.age)
print("Phone Number:", objemp.phone_number)
print("Address:", objemp.address)
print("Salary:", objemp.salary)
print("Specialization:", objemp.specialization)
objemp.print_salary()
print()

# Printing details of the Manager
print("Manager Details:")
print("Name:", objmanager.name)
print("Age:", objmanager.age)
print("Phone Number:", objmanager.phone_number)
print("Address:", objmanager.address)
print("Salary:", objmanager.salary)
print("Department:", objmanager.department)
objmanager.print_salary()


          