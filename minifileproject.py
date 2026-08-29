#MINI FILE HANDLING PROJECT
def add_note():
    note = input("Enter your note:")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved successfully")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.read()
            print("\nYour Notes:")
            print(notes)
    except FileNotFoundError:
            print("No notes found")
while True:
     
    print("\n1.Add Note")
    print("2.View Notes")
    print("3.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice") 