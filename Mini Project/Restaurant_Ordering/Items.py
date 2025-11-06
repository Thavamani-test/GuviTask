from Restaurant_Ordering.menu_items import MenuItems

class Biryani(MenuItems):
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type

    def get_item_details(self):
        return f"{self.name}"
        return f"{self.get_price()}"
        return f"{self.type} Biryani {self.get_price()}"

class Chicken65(MenuItems):
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type

    def get_item_details(self):
        return f"{self.type} Chicken65 {self.get_price()}"


class MuttonKola(MenuItems):
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type

    def get_item_details(self):
        return f"{self.type} MuttonKola {self.get_price()}"


class Drink(MenuItems):
    def __init__(self, name, price, type):
        super().__init__(name, price)
        self.type = type

    def get_item_details(self):
        return f"{self.type} Lemon Soda {self.get_price()}"

