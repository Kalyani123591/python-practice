#create a student dictionary
student = {
    "name" : "Kalyani",
    "age" : 22,
    "course" : "Python"
}
print(student)

#access the student's name 
print(student["name"])

#access age using get()
print(student.get("age"))

#change student age 
student["age"] = 21
print(student)

#add a new city as a key
student["city"] = "Hyderabad"
print(student)

#remove city using pop()
student.pop("city")
print(student)

#print all keys
print(student.keys())

#print all key-value pairs
print(student.items())

#loop through keys and values
for key,value in student.items():
    print(key, value)

#count key-value pairs
print(len(student))

#merge 2 dict
dict1 = {"a": 1, "b": 2}
dict2= {"c": 3, "d": 4}
result = dict1.copy()
result.update(dict2)
print(result)

#create dict from 2 lists
keys = ["name", "age", "city"]
values = ["Kalyani", "24", "Hyd"]
student = dict(zip(keys,values))
print(student)

#find largest and smallest
marks = {
    "Math": 85,
    "Science": 92,
    "English": 78
}
largest = max(marks.values())
print("Largest:", largest)
smallest=min(marks.values())
print("Smallest:", smallest)

#find sum of all values
total = sum(marks.values())
print("Total:", total) 

#character frequency
text = "hello"
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)

#remove duplicate values
data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 40
}
unique_values = set(data.values())
print(unique_values)

#create nested dictionary
students = {
    "student1":{
        "name": "Kalyani",
        "age": 22
    } ,
    "student2":{
        "name": "Siri",
        "age": 21
    } ,
    "studemt3":{
        "name": "Meghana",
        "age": 23
    }
}
print(students)

#access age from nested dict
print(students["student1"]["age"])