''' numbers= (10,20,30,40,50)
print(numbers)

fruits= ("apple", "banana", "mango", "orange")
print(fruits[0])
print(fruits[-1])
print(len(fruits))

print(numbers[2])

print(numbers[:3])

print(numbers[-2:])

if "apple" in fruits:
    print("Preent")
else:
    print("Not present")

print(numbers.count(20))

print(fruits.index("banana"))

tuple1= (1,2,3)
tuple2= (4,5,6)
result= tuple1 + tuple2
print(result)

result1 = tuple1 * 3
print(result1)

#convert a list into a tuple
num= [10,20,30,40]
numbers_tuple= tuple(num)
print(numbers_tuple)

#convert tuple into list
number_list= list(numbers)
print(number_list)

#create a tuple with one item
my_tuple = (10,)
print(my_tuple)

#Tuple unpacking 
data = ("Python", "Java", "SQL")
a,b,c = data
print(a, b, c)

#swap 2 variables using tuple unpacking
a= 10
b= 20
a, b = b, a
print("a=", a)
print("b=", b)

nums = (10, 15, 20, 25, 30, 35)
even = 0
odd = 0
for num1 in nums:
    if num1 % 2 == 0:
        even +=1
    else:
        odd +=1
print("Even=", even)
print("odd=", odd) '''

#remove duplicates
num2 = (1,2,2,3,4,4,5)
result2 = []
for num3 in num2:
    if num3 not in result2:
        result2.append(num3)
unique = tuple(result2)
print(unique)