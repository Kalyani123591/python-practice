#FILE HANDLING

#Create and write to a file
file = open("sample.txt", "w")
file.write("Hello Python!")
file.close()

#Read a file 
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

#Write multiple lines
file2 = open("students.txt", "w")
file2.write("Kalyani\n")
file2.write("Meghana\n")
file2.write("Siri")
file2.close()

#Read the file line by line
file2 = open("students.txt", "r")
for line in file2:
    print(line.strip())
file2.close()

#Read only the first 10 characters
file = open("sample.txt", "r")
content = file.read(10)
print(content)
file.close()

#Use readline()
file2 = open("students.txt", "r")
line1 = file2.readline()
line2 = file2.readline()
print(line1)
print(line2)
file.close()

#Use readlines()
file2 = open("students.txt", "r")
lines = file2.readlines()
print(lines)
file2.close()

#Append data to a file
file2 = open("students.txt", "a")
file2.write("Laxmi\n")
file2.close()

#Write a list of names to a file
names = ["Rama\n", "Laxmi\n", "Krishna\n"]
file = open("names.txt", "w")
file.writelines(names)
file.close()

#Check whether a file exists
import os
if os.path.exists("sample.txt"):
    print("File exists")
else:
    print("File does not exist") 

#Use with open()
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

#Write using with open()
with  open("Message.txt", "w") as file:
    file.write("Welcome to Python FileHandling")

#Count the no.of lines
with open("students.txt", "r") as file:
    lines = file.readlines()
print("Number of lines:", len(lines))

#Count the no.of words
with open("sample.txt", "r") as file:
    content = file.read
words = content.split()
print("Number of words:", len(words))

#Count characters in a file
with open("sample.txt", "r") as file:
    content = file.read()
print("Number of characters:", len(content))

#Copy contents from one file to another
with open("source.txt", "r") as source:
    content = source.read()
with open("destination.txt", "w") as destination:
    destination.write(content)
print("File copied successfully")

#Search for a word in a file
with open("sample.txt", "r") as file:
    content = file.read()
word = input("Enter word to search:")
if word in content:
    print("word found")
else:
    print("word not found")

#Replace a word in a file
with open("sample.txt","r") as file:
    content = file.read()
content = content.replace("Python", "Java")
with open("sample.txt", "w") as file:
    file.write(content)
    print("Word replaced successfully")

#Handle FileNotFoundError
try:
    with open("unknown.txt", "r") as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")

#Read only lines containing "Python"
with open("sample.txt", "r") as file:
    for line in file:
        if "Python" in line:
            print(line.strip()) 

#CSV File Handling
#Write data to a csv file
import csv
with open("students.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["Kalyani", "22", "Python"])
    writer.writerow(["Sir", "23", "Java"])

#Read a csv file
import csv
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#JSON FILE HANDLING
#Write JSON Data
import json
student = {
    "name" : "Kalyani",
    "age" : 22,
    "course" : "Python"
}
with open("student.json", "w") as file:
    json.dump(student, file, indent = 4)

#Read JSON data
import json
with open("student.json", "r") as file:
    student = json.load(file)
print(student)
print(student["name"])
print(student["course"])