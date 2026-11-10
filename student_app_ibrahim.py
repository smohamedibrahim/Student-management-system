
student_list = []

def add_student():
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")
    student_class = input("Enter Class/Grade: ")
    student_age = input("Enter Student Age: ")
    student_marks = input("Enter Student Marks: ")

    student_data = {
        "id": student_id,
        "name": student_name,
        "class": student_class,
        "age": student_age,
        "marks": student_marks
    }

    student_list.append(student_data)
    print("✔ Student details saved successfully\n")


def show_all_students():
    if len(student_list) == 0:
        print("No student data available\n")
        return

    print("---- Student Records ----")

    for student in student_list:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Class: {student['class']} | "
            f"Age: {student['age']} | "
            f"Marks: {student['marks']}"
        )
    print()


def edit_student():
    search_id = input("Enter Student ID to update: ")

    for student in student_list:
        if student["id"] == search_id:
            student["name"] = input("Update Name: ")
            student["class"] = input("Update Class: ")
            student["age"] = input("Update Age: ")
            student["marks"] = input("Update Marks: ")

            print("✔ Student record updated successfully\n")
            return

    print("Student ID not found\n")


def remove_student():
    search_id = input("Enter Student ID to remove: ")

    for student in student_list:
        if student["id"] == search_id:
            student_list.remove(student)
            print("✔ Student removed successfully\n")
            return

    print("Student ID not found\n")


def start_app():
    print("Welcome to Student Management App\n")

    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        user_option = input("Choose an option: ")

        if user_option == "1":
            add_student()

        elif user_option == "2":
            show_all_students()

        elif user_option == "3":
            edit_student()

        elif user_option == "4":
            remove_student()

        elif user_option == "5":
            print("Application closed. Thank you!")
            break

        else:
            print("Invalid option. Try again.\n")


start_app()
