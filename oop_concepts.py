#1.ENCAPSULATION
#Bank Account
class BankAccount():
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("withdrawal is successful")
        else:
            print("Insufficient balance")
    def check_bal(self):
        print("Balance:", self.__balance)
account = BankAccount(10000)
account.deposit(2000)
account.withdraw(3000)
account.check_bal()

#2.Employee- Private Salary
class Employee:
    def __init__(self, salary):
        self.__salary = salary
    def set_salary(self, salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary
employee = Employee(30000)
print(employee.get_salary())
employee.set_salary(40000)
print(employee.get_salary())  

#INHERITANCE
#1.Vehicle-> car and bike
class Vehicle:
    def start(self):
        print("Vehicle is starting")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")
class Bike(Vehicle):
    def ride(self):
        print("Bike is starting")
car =Car()
bike = Bike()
car.start()
car.drive()
bike.start()
bike.ride()

#2.Mutilevel Inheritance
class Animal:
    def eat(self):
        print("Animal eats")
class Mammal(Animal):
    def walk(self):
        print("Mammal walks")
class Dog(Mammal):
    def bark(self):
        print("Dog barks")
dog = Dog()
dog.eat()
dog.walk()
dog.bark()

#3.Multiple Inheritance
class Father:
    def father_method(self):
        print("Father's method")
class Mother:
    def mother_method(self):
        print("Mother's method")
class Child(Father, Mother):
    def child_method(self):
        print("Child's method")
child = Child()
child.father_method()
child.mother_method()
child.child_method()  

#POLYMORPHISM
#1.Car and Bike -- speed()
class Car:
    def speed(self):
        print("Car speed is 120 km/h")
class Bike:
    def speed(self):
        print("Bike spped is 80 km/h")
car = Car()
bike = Bike()
car.speed()
bike.speed()

#Method Overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
animal = Animal()
dog = Dog()
animal.sound()
dog.sound() 

#ABSTRACT
#1.Abstract Shape
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def area(self):
        radius = 5
        return 3.14 * radius * radius
class Rectangle(Shape):
    def area(self):
        length = 10
        width = 5
        return length * width
circle = Circle()
rectangle = Rectangle()
print("Circle area:", circle.area())
print("Rectangle area:", rectangle.area())

#2.Abstract Payment System
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CreditCardPayment(Payment):
    def pay(self,amount):
        print("Paid", amount, "using Credit Card")
class UPIPayment(Payment):
    def pay(self, amount):
        print("Paid", amount , "using UPI")
credit_card = CreditCardPayment()
upi = UPIPayment()
credit_card.pay(1000)
upi.pay(500)