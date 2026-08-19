#create  a student class and object
class Student:               #creates class
    pass
student1 = Student()         #creates obj
print(student1) 

#student with name,age,course
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
student1 = Student("Kalyani", 22, "Python")
print(student1.name)
print(student1.age)
print(student1.course)

#Person class with display() method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
person1 = Person("Kalyani", 22)
person1.display()

#Calculator class
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b
calc = Calculator()
print(calc.add(10, 5))
print(calc.subtract(10, 5))
print(calc.multiply(10, 5))
print(calc.divide(10, 5))

#Rectangle- Area and Perimeter
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
rectangle = Rectangle(10, 5)
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())

#Employee Class
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    def display(self):
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.emp_id)
employee1 = Employee("kalyani", 101, 30000)
employee1.display()  

#Bank account class 
class BankAccount:
    def __init__(self, acc_holder, acc_num, balance):
        self.acc_holder = acc_holder
        self.acc_num = acc_num
        self.balance = balance
    def display(self):
        print("Account holder:", self.acc_holder)
        print("Account Number:", self.acc_num)
        print("Balance:", self.balance)
account1 = BankAccount("Kalyani", 12345, 1000)
account1.display()