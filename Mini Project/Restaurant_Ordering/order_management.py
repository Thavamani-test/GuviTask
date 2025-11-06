from Restaurant_Ordering.menu_items import Menu_Items
class Order:
    TAX_RATE = 0.05
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        sub_total = sum(item.get_price() for item in self.items)
        tax = sub_total * self.TAX_RATE
        return sub_total+tax

def show_bill(self):
    total = self.calculate_total()
    print(f"--------------Bil--------------")
    for item in self.items:
        print(item.get_item_details())
    total = self.calculate_total()
    print(f"Total (incl. GST): ${round(total, 2)}")
    return total

if __name__ == "__main__":
    biryani = Biryani("Biryani", 100, "Dum")
    chicken65= Chicken65("Chicken 65", 100, "Boneless")
    muttonkola= MuttonKola("MuttonKola Ball", 200, "Big Ball")
    drink= Drink("Lemon Soda", 80, "sweet")

    order = Order()
    order.add_item(biryani)
    order.add_item(chicken65)
    order.add_item(muttonkola)
    order.add_item(drink)

    total_amount = order.show_bill()

    payment_method == CardPayment()
    payment_method.make_payment(total_amount)





