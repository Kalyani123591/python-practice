def hello():
    print("Hello, Pyhton!")
hello()

#print 1 to 10
def print_numbers():
    for i in range(1, 11):
        print(i)
print_numbers()

#print even no.s 1 to 20
def even_numbers():
    for i in range(1,21):
        if i % 2 == 0:
            print(i)
even_numbers()

#print a msg 3 times
def welcome():
    for i in range(3):
        print("Welcome to Pyhton.")
welcome()

#function with a name arg
def greet(name):
    print("hello", name)
greet("Kalyani")

#add,sub,multiply,divide
def asmd(a,b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
asmd(20, 10)

#PARAMETERS AND RETURN VALUES:
#return square value
def square(number):
    return number ** 2
result= square(5)
print(result)

#return largest of 3 no.s
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(largest(20, 60, 10))

#check even or odd
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_odd(345))

#Factorial using function
def factorial(num1):
    result1 = 1
    for i in range(1, num1 + 1):
        result1 *= i
    return result1
print(factorial(5))

#return sum of a list
def list_sum(numbers1):
    return sum(numbers1)
print(list_sum([10, 20, 30]))

#find seconnd-largest number
def second_largest(num2):
    num2 = list(set(num2))
    num2.sort()
    return num2[-2]
print(second_largest([10, 50, 30, 20, 40]))

#return grade based on marks
def get_grade(marks):
    if marks >= 90:
        return "A"
    if marks >= 75:
        return "B"
    if marks >= 50:
        return "C"
    if marks >= 35:
        return "D"
    else:
        return "F"
print(get_grade(96))