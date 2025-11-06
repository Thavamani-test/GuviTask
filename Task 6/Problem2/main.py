# Base class defining
class Employee:
    def __init__(self, name, base_salary):
#Using Encapsulation to act as private
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
    #Base salary calculation to be overridden by subclasses
        return self.base_salary

    def get_employee_details(self):
        return f"Employee: {self.name},Salary: {self.calculate_salary()}"

# Subclass 1: RegularEmployee
class RegularEmployee(Employee) :
    def __init__(self, name, base_salary,bonus, deductions):
        # super() keyword is used to access parent class content
        super().__init__(name, base_salary)
        self.bonus = bonus
        self.deductions = deductions

    # salary= base_salary +bonus - deductions
    def calculate_salary(self):
        return self.base_salary + self.bonus - self.deductions


# Subclass 2: ContractEmployee
class ContractEmployee(Employee) :
    def __init__(self, name, rate_per_hour, worked_hours):
        super().__init__(name, base_salary=0) #base_salary not used
        self.rate_per_hour = rate_per_hour
        self.worked_hours = worked_hours

    def calculate_salary(self):
     #salary = rate_per_hour* worked_hours
        return self.rate_per_hour * self.worked_hours


# Subclass 3: Manager
class Manager(Employee) :
    def __init__(self, name, base_salary, allowance, bonus_as_per_performance):
        super().__init__(name, base_salary)
        self.allowance = allowance
        self.bonus_as_per_performance = bonus_as_per_performance

    def calculate_salary(self):
    # salary= base_salary +allowance + bonus for performance
        return self.base_salary + self.allowance + self.bonus_as_per_performance

#main class
if __name__ == "__main__":
    employees =[
        RegularEmployee("Deepa", 50000, bonus=5000, deductions=2000),
        ContractEmployee("Vivek", rate_per_hour=400, worked_hours=120),
        Manager("Sara", base_salary=80000, allowance=15000, bonus_as_per_performance=10000)
                ]

    print("---------------Employee Salary Info----------------")
    for emp in employees:
    #Polymorphism- same method name calculate_salary(), behaves differently based on the logic given in each class
        print(f" Calculated salary for {emp.name} : {emp.calculate_salary()}")
