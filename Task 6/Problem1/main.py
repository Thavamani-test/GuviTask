# Base class defining
class BankAccount:
    def __init__(self, account_number, balance=0):
#Using Encapsulation to act as private
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0 :
            self.__balance += amount
            print(f"Deposit amount: {amount}. Updated after deposit balance: {self.__balance}")
        else:
            print("Deposit amount can't be negative")

    def withdraw(self,amount):
        if amount <= 0:
            print("Withdraw amount can't be negative")
            return

        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw amount: {amount}. Updated withdrawal balance: {self.__balance}")
        else:
            print("Insufficient balance")

    def get_account_number(self):
            return self.__account_number

    def get_balance(self):
        # getter method to keep balance details within class
            return self.__balance

    def set_balance(self, new_balance):
        # setter method to keep balance details within class
        self.__balance = new_balance


# Subclass 1: SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.05):
        super().__init__(account_number, balance)
        #self.__account_number = account_number
        #self.__balance = balance
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        print(f"Calculated Interest: {interest}")
        return interest

# Subclass 2: CurrentAccount
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance=0, minimum_balance=500):
        #super() keyword is used to access parent class content
        super().__init__(account_number, balance)
        #self.__account_number = account_number
        #self.__balance = balance
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount can't be negative")
            return

#Checking whether the amount requested to withdraw should not greater than the account balance
    #and also should not affect minimum balance
        if self.get_balance() - amount < self.minimum_balance:
            print("Insufficient Balance to Withdraw amount")
        else:
            updated_balance =self.get_balance() - amount
            self.set_balance(updated_balance)
            print(f"Withdraw amount: {amount}. Updated balance after withdrawal : {self.get_balance()}")

#main class
if __name__ == "__main__":
    # Object Creation for SavingsAccount Subclass
    sa = SavingsAccount("123456789", 100, 0.05)
    sa.deposit(1000)
    sa.calculate_interest()
    sa.withdraw(500)
    print("--------------Account Transaction Info------------")
    print(f"Final Savings Account balance: ", sa.get_balance())
    print('\n')

    # Object Creation for CurrentAccount Subclass
    ca = CurrentAccount("123456789", 5000, minimum_balance=500)
    ca.deposit(1000)
    ca.withdraw(7000) #This will display warning if it drops below minimum balance
    ca.withdraw(1000) #This should work
    print(f"Final Current Account balance: ", ca.get_balance())

