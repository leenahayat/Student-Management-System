
students = []

def add_student():
    name = input("Enter name: ")
    rollno = input("Enter roll no: ")
    marks = input("Enter marks: ")

    student = {
        "name": name,
        "rollno": rollno,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No record found.")
    else:
        print("\n{:<15} {:<15} {:<10}".format("Name", "Roll No", "Marks"))
        print("-" * 40)

        for s in students:
            print("{:<15} {:<15} {:<10}".format(s["name"], s["rollno"], s["marks"]))

def search_student():
    roll = input("Enter roll no to search: ")
    for s in students:
        if s["rollno"] == roll:
            print("Found:", s)
            return
    print("Student not found :(")

def delete_student():
    roll = input("Enter roll no to delete: ")
    for s in students:
        if s["rollno"] == roll:
            students.remove(s)
            print("Deleted successfully!")
            return
    print("Student not found.")

while True:
    print("\n1. Add\n2. View\n3. Search\n4. Delete\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
