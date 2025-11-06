class MenuItems:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_item_details(self):
        return f"{self.__name}: ${self.__price}"
