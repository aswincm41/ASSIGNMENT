#CLASS

#QS1

class StringProcessor:
    def get_string_from_console(self):
        self.input_string = input("Enter a string: ")

    def print_uppercase_string(self):
        if hasattr(self, 'input_string'):
            print("Uppercase String:", self.input_string.upper())
        else:
            print("No input string. Use get_string_from_console() first.")
processor = StringProcessor()
processor.get_string_from_console()
processor.print_uppercase_string()


#QS2

class MyClass:
    class_parameter = "Class Parameter" 

    def __init__(self, instance_parameter):
        self.instance_parameter = instance_parameter

    def display_parameters(self):
        print("Class Parameter:", MyClass.class_parameter)
        print("Instance Parameter:", self.instance_parameter)

instance1 = MyClass("Instance 1")
instance2 = MyClass("Instance 2")
print("Parameters for instance1:")
instance1.display_parameters()
print("\nParameters for instance2:")
instance2.display_parameters()


#QS3

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius**2

radius_value = 5
circle_instance = Circle(radius_value)

area_result = circle_instance.compute_area()

print(f"Circle with radius {radius_value}")
print(f"Area: {area_result:.2f}")


#QS4

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient funds. Cannot withdraw more than the available balance.")
        else:
            print("Invalid withdrawal amount. Please withdraw a positive amount.")
account = BankAccount(initial_balance=1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(800)
account.deposit(-100)

#QS5

class Shape:
    def __init__(self):
        pass 

    def area(self):
        return 0 
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length ** 2 
shape_instance = Shape()
square_instance = Square(length=4)

print("Area of the Shape:", shape_instance.area()) 
print("Area of the Square:", square_instance.area()) 
