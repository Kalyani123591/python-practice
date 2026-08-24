#EXCEPTION HANDLING

#Handle Division by zero
try:
    a = 10
    b = 0
    result = a / b
    print(result)
except ZeroDivisionError:
    print("cannot divide by zero") 

#Handle invalid  input
try:
    num = int(input("enter a number:"))
    print("You entered:", num)
except ValueError:
    print("Please enter a valid number")

#Handle ValueError
try:
    number = int("hello")
    print(number)
except ValueError:
    print("Cannot convert string into integer")

#Handle IndexError
numbers = [10, 20, 30]
try:
    print(numbers[5])
except IndexError:
    print("Index does not exist")

#Handle KeyError
student = {
    "name": "Kalyani",
    "age": 22
}
try:
    print(student["age"])
    print(student["course"])
except KeyError:
    print("Key does not exist")

#Handle TypeError
try:
    result = 10 + "20"
    print(result)
except TypeError:
    print("Cannot add integer and string") 

#Multiple except Blocks
try:
    num = int(input("Enter number:"))
    result = 10 / num
    print(result)
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero")

#try-except-else
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", number)

#try-except-finally
try:
    num1 = 10 / 2
    print(num1)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Program completed")

#Catch any unexcepted exception
try:
    num2 = 10 / 0
except Exception as e:
    print("An error occurred:", e) 

#Safe Division Function
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
print(divide(10, 2))
print(divide(10, 0))

#Keep asking until valid integer
while True:
    try:
        num = int(input("Enter an integer:"))
        print("Valid number:", num)
        break
    except ValueError:
        print("Invalid input. Try again.")

#Handle ValueError and ZeroDivisionError
try:
    a = int(input("Enetr 1st num:"))
    b = int(input("Enter 2nd num:"))
    print("Result:", a / b)
except ValueError:
    print("Pleasee enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero")

#Safely access a List
number = [10, 20, 30]
try:
    index = int(input("Enter index"))
    print("Value:", number[index])
except ValueError:
    print("Enter a valid integer index")
except IndexError:
    print("Index is out of range")

#Safely access a dict
student  = {
    "name": "Siri",
    "age": 22,
    "course": "Python"
}
try:
    key = input("Enter key: ")
    print("Value:", student[key])
except KeyError:
    print("Key not found")

#Custom Exception- Insufficient Balance
class InsufficientBalanceError(Exception):
    pass
balance = 5000
withdraw = 7000
try:
    if withdraw > balance:
        raise InsufficientBalanceError("Insufficient balance")
    balance -= withdraw
    print("Remaining balance:", balance)
except InsufficientBalanceError as e:
    print(e)

#Raise Exception for Negative Number
def check_num(number):
    if num < 0:
        raise ValueError("Number cannot be negative")
    print("Number is valid")
try:
    check_num(-5)
except ValueError as e:
    print(e)

#Demonstrating raise
def check_age(age):
    if age < 18:
        raise ValueError("You must be 18 or older")
    return "eligible"
try:
    print(check_age(15))
except ValueError as e:
    print("Error:", e)