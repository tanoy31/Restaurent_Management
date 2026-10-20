class Menu:
    def __init__(self):
        self.item=[]

    def add_item(self,item):
        self.item.append(item)
        print(f"Item {item.name} added successfully")

    def find_item(self,item_name):
        for item in self.item:
            if item.name.lower()==item_name.lower():
                return item
        return None

    def remove_item(self,item_name):
        item=self.find_item(item_name)
        if item:
            self.item.remove(item)
            print(f"Item {item_name} removed successfully")
        else:
            print(f"Item {item_name} not found in the menu")

    def show_menu(self):
        if not self.item:
            print("Menu is empty.")
        else:
            print("*****Menu*****")
            print("Name\tPrice\tQuantity")
            for item in self.item:
                print(f"{item.name}\t{item.price}\t{item.quantity}")