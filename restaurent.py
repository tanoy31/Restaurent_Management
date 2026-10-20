from menu import Menu

class Restaurent:
    def __init__(self,name):
        self.name=name
        self.employees=[]
        self.menu=Menu()

    def add_employee(self,employee):    
        self.employees.append(employee)
        print(f"Employee {employee.name} added successfully")

    def view_employees(self):
            if not self.employees:
                print("No employees found.")
            else:
                print("List of Employees:")
                for employee in self.employees:
                    print(f"Name: {employee.name}, Phone: {employee.phone}, Age: {employee.age}, Designation: {employee.designation}, Salary: {employee.salary}")
