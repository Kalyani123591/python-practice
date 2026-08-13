students=[]

#Module1 : Add a student
def add_student():
    name= input("Enter student name: ")
    age= int(input("Enter age: "))
    marks= float(input("Enter marks: "))
    student={
        "name": name,
        "age": age,
        "marks": marks
    }
    students.append(student)
    print("Student added successfully!")

#Module2 : Display students
def display_students():
    if len(students) == 0:
        print("No students available.")
    else:
        print("\nStudent details:")
        for student in students:
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])

#Module3 : Calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

#Module4 : Search student
def search_student():
    name= input("Enter student name to search: ")
    for student in students:
        if student["name"].lower()== name.lower():
            grade= calculate_grade(student["marks"])
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"]) 
            print("Grade:", grade)
            return
    print("student not found")

#Main Module
def main():
    while True:
        print("\n Student Management System ")
        print("1. Add Student")
        print("2. Display Student")
        print("3. Search Student")
        print("4. Exit")

        choice = input("enter your choice:")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("END")
            break
        else:
            print("Invalid choice.Please try again.")

#start the program
main()