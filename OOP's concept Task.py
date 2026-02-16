#Question:1
print('Question:1')
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'You have deposited {amount}. Total bank balance is {self.__balance}')

        else:
            print(f'You have not deposited')


    def withdraw(self, amount):

        if amount > 0:
            self.__balance -= amount
            print(f'You have withdrawn {amount}, remaining balance: {self.__balance}')
        else:
            print(f'You have Insufficient balance')

    def get_balance(self):
        return self.__balance

class SavingsAccount(BankAccount):
    def __init__(self,aacount_number,balance,interest):
        super().__init__(aacount_number,balance)
        self.interest = interest

    def interest_calculate(self):
        Interest_value = (self.get_balance() * self.interest) / 100
        print(f'Interest of the account balance is {Interest_value}')
        return Interest_value

class CurrentAccount(BankAccount):
    def __init__(self,account_number,balance,minimum_balance):
        super().__init__(account_number,balance)
        self.minimum_balance = minimum_balance

    def minimumBal_check(self):
        if self.get_balance() >= self.minimum_balance:
            print(f'Account have sufficient balance. Your Balance is Rs {self.get_balance()}')

        else:
            print('Account have insufficient balance')

savings = SavingsAccount('XYZ123',5000,2)
savings.deposit(2000)
savings.withdraw(1000)
savings.interest_calculate()
current_acct = CurrentAccount('XYZ123',5000,1000)
current_acct.withdraw(500)
current_acct.minimumBal_check()

# Question:2
print('\n Question#2')
class Employee:
    def __init__(self,Name, Basic_Salary):
        self.Name = Name
        self.Basic_Salary = Basic_Salary

    def calculate_salary(self):
        return self.Basic_Salary

class RegularEmployee(Employee):
    def __init__(self,Name,Basic_Salary,Bonus_per):
        Employee.__init__(self,Name,Basic_Salary)
        self.Bonus_per = Bonus_per

    def calculate_salary(self):
        salary = (self.Basic_Salary * self.Bonus_per)
        print(f'Regular Employee Salary: {salary}')
        return salary

class ContractEmployee(Employee):
    def __init__(self,Name,Basic_salary,working_hour):
        Employee.__init__(self,Name,Basic_salary)
        self.working_hour = working_hour


    def calculate_salary(self):

        salary = self.working_hour * self.Basic_Salary
        print(f'Contract Employee Salary: {salary}')
        return salary

class Manager(Employee):
    def __init__(self,Name,Basic_Salary,Bonus_per):
        Employee.__init__(self,Name,Basic_Salary)
        self.Bonus_per = Bonus_per

    def calculate_salary(self):
        salary = (self.Basic_Salary * self.Bonus_per)
        print(f'Manager Employee Salary: {salary}')
        return salary

Reg_Empl = RegularEmployee('Nandhini',10000, 3)
Reg_Empl.calculate_salary()
Cont_Empl = ContractEmployee('Gokilavani',1000, 20 )
Cont_Empl.calculate_salary()
Manager_Empl = Manager('Rishani',15000,5)
Manager_Empl.calculate_salary()


#Question:3
print('\n Question#3')
class Vehicle:
    def __init__(self,model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_salary(self):
        return self.rental_rate


class Car(Vehicle):
    def __init__(self,model,rental_rate,num_hour):
        Vehicle.__init__(self,model,rental_rate)
        self.num_hour = num_hour

    def calculate_rent(self):
        if self.num_hour >= 48:
            self.rental_rate = (self.rental_rate * self.num_hour)
            discount_amount = self.rental_rate * (2 / 100)
            rent = self.rental_rate - discount_amount

        elif self.num_hour >= 24 and self.num_hour<48:
            self.rental_rate = (self.rental_rate * self.num_hour)
            discount_amount = self.rental_rate * (1 / 100)
            rent = self.rental_rate - discount_amount

        else:
            self.rental_rate = (self.rental_rate * self.num_hour)
            discount_amount = self.rental_rate * (0.5/100)
            rent = self.rental_rate - discount_amount

        print(f'Car rent is Rs: {rent}')

class Bike(Vehicle):
    def __init__(self,model,rental_rate,num_hour):
        Vehicle.__init__(self,model,rental_rate)
        self.num_hour = num_hour


    def calculate_rent(self):
        if self.num_hour >= 48:
            self.rental_rate = (self.rental_rate * self.num_hour)
            discount_amount = self.rental_rate * (3 / 100)
            rent = self.rental_rate - discount_amount

        elif self.num_hour >= 24 and self.num_hour<48:
            self.rental_rate = (self.rental_rate * self.num_hour)
            discount_amount = self.rental_rate * (1.5 / 100)
            rent = self.rental_rate - discount_amount

        else:
            self.rental_rate = (self.rental_rate * self.num_hour)
            discount_amount = self.rental_rate * (0.5 / 100)
            rent = self.rental_rate - discount_amount

        print(f'Bike rent is Rs: {rent}')



class Truck(Vehicle):
    def __init__(self,model,rental_rate,num_hour):
        Vehicle.__init__(self,model,rental_rate)
        self.num_hour = num_hour

    def calculate_rent(self):
        if self.num_hour >= 48:
            self.rental_rate = (self.rental_rate * self.num_hour)
            discount_amount = self.rental_rate * (1.5 / 100)
            rent = self.rental_rate - discount_amount

        elif self.num_hour >= 24 and self.num_hour<48:
            self.rental_rate = (self.rental_rate * self.num_hour)
            discount_amount = self.rental_rate * (1 / 100)
            rent = self.rental_rate - discount_amount

        else:
            self.rental_rate = (self.rental_rate * self.num_hour)
            discount_amount = self.rental_rate * (0.5 / 100)
            rent = self.rental_rate - discount_amount

        print(f'Truck rent is Rs: {rent}')

car_obj = Car('Toyota',700,6)
car_obj.calculate_rent()

bike_obj = Bike('Royal Enfield',500,3)
bike_obj.calculate_rent()

truck_obj = Truck('Mahindra Veero',1000,5)
truck_obj.calculate_rent()