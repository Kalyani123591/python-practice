#Class variable & Instance variable
class Student:
    school_name = "ABC School"   #class variable
    def __init__(self, name):
        self.name = name         #instance variable
student1 = Student("Kalyani")
student2 = Student("Laxmi")
print(student1.name)
print(student1.school_name)
print(student2.name)
print(student2.school_name)

#Employee - Class & Instance Variables
class Employee:
    company = "ABC Technologies"    #class variable
    def __init__(self, name):
        self.name = name            #instance variable
employee1 = Employee("Kalyani")
employee2 = Employee("Siri")
print(employee1.name)
print(employee1.company)
print(employee2.name)
print(employee2.company) 

#Count no.of objects created
class Student:
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1
stu1 = Student("Kalyani")
stu2 = Student("Siri")
stu3 = Student("Maggie")
print("No.of Students:", Student.count)

#__str__() Magic Method
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"
book = Book("Python Basics", "John")
print(book)

#__str__() with Student
class Stu:
    def __init__(self, name, course):
        self.name = name
        self.course = course
    def __str__(self):
        return f"Name: {self.name}, Course: {self.course}"
stu = Stu("Kalyani", "Python")
print(stu)

#__len__() Magic Method
class Course:
    def __init__(self, subjects):
        self.subjects = subjects
    def __len__(self):
        return len(self.subjects)
course = Course(["Python", "SQL", "HTML", "Git"])
print(len(course))

#@property - Bank Balance
class bankAccount:
    def __init__(self, balance):
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")
account = bankAccount(10000)
print("Balance:", account.balance)
account.balance = 15000
print("Updated balance:", account.balance) 


#LIBRARY MANAGEMENT
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    def borrow(self):
        if self.available:
            self.available = False
            print("Book borrowed successfully")
        else:
            print("Book is already borrowed")
    def return_book(self):
        self.available = True
        print("Book returned successfully")
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        if self.available:
            print("Status: Available")
        else:
            print("Status: Not Available")
book = Book("Python Basics", "Joohn")
book.display()
book.borrow()
book.display()
book.return_book()
book.display()

#Shopping Cart
class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self, item, price):
        self.items.append((item, price))
        print(item, "added to cart")
    def display_items(self):
        print("\n Items in cart:")
        for item, price in self.items:
            print(item, "-", price)
    def total_price(self):
        total = 0
        for item, price in self.items:
            total += price
        return total
cart = ShoppingCart()
cart.add_item("Laptop", 50000)
cart.add_item("Mouse", 1000)
cart.add_item("Kayboard", 2000)
cart.display_items()
print("Total Price:", cart.total_price())

#Simple ATM System
class ATM:
    def __init__(self, balance, pin):
        self.__balance = balance
        self.__pin = pin
    def check_balance(self):
        print("Balance:", self.__balance)
    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited:", amount)
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")
atm = ATM(10000, 1234)
atm.check_balance()
atm.deposit(2000)
atm.withdraw(3000)
atm.check_balance()