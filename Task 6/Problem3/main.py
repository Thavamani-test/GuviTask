#Base class
class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate #base rate as per day

    def calculate_rental(self, no_of_days):
        # Base salary calculation to be overridden by subclasses
        return self.rental_rate * no_of_days

    def get_vehicle_details(self):
        return f"{self.__class__.__name__} Model: {self.model}"


#Subclass 1: Car
class Car(Vehicle):
    def __init__(self, model, rental_rate,tax_rate=0.4):
        # super() keyword is used to access parent class content
        super().__init__(model, rental_rate)
        self.tax_rate = tax_rate

    def calculate_rental(self, no_of_days):
            #Rental rate = base rate * number of days + tax rate
            base_rate = self.rental_rate * no_of_days
            total_rent=base_rate +(base_rate * self.tax_rate)
            return total_rent


#Subclass 2: Bike
class Bike(Vehicle):
    def __init__(self, model, rental_rate,helmet_rate=100):
        super().__init__(model, rental_rate)
        self.helmet_rate = helmet_rate

    def calculate_rental(self, no_of_days):
        #Rental rate = base rate * number of days + helmet_rate
        base_rate = self.rental_rate * no_of_days
        total_rent = base_rate + (base_rate * self.helmet_rate)
        return total_rent

#Subclass 3: Truck
class Truck(Vehicle):
    def __init__(self, model, rental_rate,load_capacity):
        super().__init__(model, rental_rate)
        self.load_capacity = load_capacity #in tons

    def calculate_rental(self, no_of_days):
        # Rental rate = base rate * number of days + additional charge for heavy load
        additional_charge =0
        if self.load_capacity > 10: # if truck is large
            additional_charge = 500 * no_of_days  # heavy load surcharge per day
        return (self.rental_rate * no_of_days) + additional_charge


#main class
if __name__ == "__main__":
    vehicles =[
        Car("Hyundai Kia", rental_rate=3000, tax_rate=0.4),
        Bike("Yamaha R15", rental_rate=500, helmet_rate=100),
        Truck("Tata Prima 5530.S", rental_rate=5000, load_capacity=15)
        ]

    rental_days=2
    print("---------------Vehicle Rent Calculation------------")
    for v in vehicles:
        print(f" Vehicle model is {v.model}  Number of days in rental :{rental_days} ")
        print(f"Total rental fare: {v.calculate_rental(rental_days):}")
