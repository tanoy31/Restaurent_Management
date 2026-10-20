from food_item import FoodItem
from menu import Menu
from orders import Orders
from restaurent import Restaurent 
from users import Customer,Employee,Admin

restaurent1=Restaurent('Kacci Dine')

def admin_menu():
    name=input("Enter your name: ")
    phone=input("Enter phone number: ")
    email=input("Enter email: ")
    address=input("Enter address: ")
    admin=Admin(name=name,phone=phone,email=email,address=address)

    while True:
        print(f'Welcome {admin.name}')
        print('1. Add item')
        print('2. Add employee')
        print('3. View items')
        print('4. View employees')
        print('5. Delete item')
        print('6. Exit')

        choice=int(input('Enter your choice: '))
        if choice==1:
            item_name=input('Enter item name: ')
            item_price=int(input('Enter price: '))
            item_quantity=int(input("Enter quantity: "))

            item=FoodItem(item_name,item_price,item_quantity)

            admin.add_new_item(restaurent1,item)

        elif choice==2:
            employee_name=input('Enter employee name: ')
            employee_phone=input('Enter employee phone: ')
            employee_email=input('Enter employee email: ')
            employee_address=input('Enter employee address: ')
            employee_age=input('Enter employee age: ')
            employee_designation=input('Enter employee designation: ')
            employee_salary=input('Enter employee salary: ')
            
            employee=Employee(employee_name,employee_phone,employee_email,employee_address,employee_age,employee_designation,employee_salary)

            admin.add_employee(restaurent1,employee)

        elif choice==3:
            admin.view_menu(restaurent1)

        elif choice==4:
            admin.view_employees(restaurent1)

        elif choice==5:
            item_name=input("Enter item name want to delete: ")
            admin.remove_item(restaurent1,item_name)

        elif choice==6:
            break

        else:
            print('Invalid input')

def customer_menu():
    name=input("Enter your name: ")
    phone=input("Enter phone number: ")
    email=input("Enter email: ")
    address=input("Enter address: ")
    customer=Customer(name=name,phone=phone,email=email,address=address)

    while True:
        print(f'Welcome {customer.name}')
        print('1. View menu')
        print('2. Add item to cart')
        print('3. View cart')
        print('4. Pay bill')
        print('5. Exit')

        choice=int(input('Enter your choice: '))
        if choice==1:
            customer.view_menu(restaurent1)

        elif choice==2:
            item_name=input('Enter item name: ')
            item_quantity=int(input("Enter quantity: "))
            customer.add_to_cart(restaurent1,item_name,item_quantity)

        elif choice==3:
            customer.view_cart()

        elif choice==4:
            amount=int(input("Enter payable amount: "))
            customer.paybill(amount)

        elif choice==5:
            break

        else:
            print('Invalid input')

while True:
    print('Welcome!!')
    print('1. Admin')
    print('2. Customer')
    print('3. Exit')

    choice=int(input('Enter your choice: '))

    if choice==1:
        admin_menu()

    elif choice==2:
        customer_menu()

    elif choice==3:
        break

    else:
        print('Invalid Input')