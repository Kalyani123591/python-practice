'''num= [10,20,30,40,50]
print(num)

#print first number
print(num[0])
#print last number
print(num[-1])

#length of list
print(len(num))

#change an element
num[2]= 60
print(num)

#add an element- append
num.append(70)
print(num)

#add an element at a specific position
num.insert(3, 90)
print(num)

#remove an element
num.remove(10)
print(num)

#remove last element using pop
num.pop()
print(num)

if 40 in num:
    print("present")
else:
    print("not present")

#sort in ascending order
numbers = [40,10,30,20,50]
numbers.sort()
print(numbers)

#sort in descending order
numbers.sort(reverse=True)
print(numbers)

#reverse a list
numbers.reverse()
print(numbers)

#count elements
print(numbers.count(10))

#position of an element
print(numbers.index(30))

#join 2 lists
list1=[1,2,3]
list2=[4,5,6]
result= list1 + list2
print(result)

#find largest and smallest
print("Largest: ", max(numbers))
print("Smallest: ", min(numbers))

#print first 3 elements
print(num[:3])

#print last 3 elements
print(num[-3:])

#reverse a lsit using slicing
print(num[::-1]) '''

#find the sum
numbers=[10,20,30,40,50]
print(sum(numbers))

#find the average
average= sum(numbers) / len(numbers)
print("Average: ", average)

#find largest and smallest without max() and min()
number=[10,50,20,40,30,5]
largest= number[0]
for number1 in number:
    if number1 > largest:
        largest = number1
print("Largest: ",largest)

smallest= number[0]
for number2 in number:
    if number2 < smallest:
        smallest = number2
print("Smallest: ", smallest)

#remove duplicates
numbers1=[1,2,2,3,3,4]
result=[]
for num1 in numbers1:
    if num1 not in result:
        result.append(num1)
print(result)

#even numbers 1 to 20
even_numbers= [x for x in range(1,21) if x % 2 == 0]
print(even_numbers)