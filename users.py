from abc import ABC
from orders import Orders
class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address

class Admin(User):
    def __init__(self,name,phone,email,address):
        super().__init__(name,phone,email,address)
        self.employees=[]

    def add_employee(self,restaurent,employee):
        restaurent.add_employee(employee)

    def view_employees(self,restaurent):
        restaurent.view_employees()

    def add_new_item(self,restaurent,item):
        restaurent.menu.add_item(item)

    def remove_item(self,restaurent,item):
        restaurent.menu.remove_item(item)

    def view_menu(self,restaurent):
        restaurent.menu.show_menu()

class Employee(User):
    def __init__(self,name,phone,email,address,age,designation,salary):
        super().__init__(name,phone,email,address)
        self.age=age
        self.designation=designation 
        self.salary=salary

class Customer(User):
    def __init__(self,name,phone,email,address):
        super().__init__(name,phone,email,address)
        self.cart=Orders()

    def view_menu(self,restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self,restaurent,item_name,quantity):
        item=restaurent.menu.find_item(item_name)
        if item:
            if quantity>item.quantity:
                print("Item quantity exceeded")
            else:
                item.quantity=quantity
                self.cart.add_item(item)
                print('Item added')
        else:
            print("Item not found")

    def view_cart(self):
        print('*****Cart*****')
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
        print(f'Total price : {self.cart.total_price()}')

    def paybill(self,amount):
        if(amount>=self.cart.total_price()):
            print("Payment successful")
            self.cart.clear()
        else:
            need=self.cart.total_price()-amount
            print(f"Insufficient amount please enter {need} taka more")



