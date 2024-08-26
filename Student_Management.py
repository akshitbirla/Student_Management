class Student:
    def __init__(self, name: str, age: int, address: str, marks: int) -> None:
        self.name = name
        self.age = age
        self.address = address
        self.marks = marks

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        try:
            name = input('Enter name: ')
            age = int(input('Enter age: '))
            address = input("Enter address: ")
            marks = int(input('Enter marks: '))
        except ValueError as error:
            print(error)
            print("You didnt enter a valid input")

        student = Student( name, age, address, marks)
        self.students.append(student)      ## Append is use to add things to a list
        print("Student successfully added")
        return student
    
    def view_student(self):
        if len(self.students) == 0:
            print("No students found")
        else:
            view_type = input("All students or one student? (all/one):")
            if view_type == "all":
                for student in self.students:
                    print(f"Name: {student.name}\n Age: {student.age}\n Address: {student.address}\n Marks: {student.marks}")
            if view_type == "one":
                name = input("Enter the name of student you want to see: ")
                for student in self.students:
                    if student.name == name:
                        print(f"Name: {student.name}\n Age: {student.age}\n Address: {student.address}\n Marks: {student.marks}")

    def delete_student(self):
        name = input("Enter the name of student you want to delete: ")
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print("Student successfully deleted")
                return self.students

    def update_student(self):
        name = input("Enter the name of student you want to update: ")
        for student in self.students:
            if student.name == name:
                print("What do you want to update? ")
                print("1. Name ")
                print("2. Age ")
                print("3. Address ")
                print("4. marks ")
                try:
                    choice = int(input("Enter your choice: "))
                except ValueError as err:
                    print(err)
                    print("You did not enter a valid input")
                if choice == 1:
                    student.name = input('Enter name: ')
                elif choice == 2:
                    student.age = int(input('Enter age: '))
                elif choice == 3:
                    student.address = input("Enter address: ")
                elif choice == 4:
                    student.marks = int(input('Enter marks: '))
                else: 
                    print("Enter a valid choice ")
                print("Student successfully updated")
                return student 
        print("Student not found")

print("Welcome to Student Management System")
system = StudentManagementSystem()

while True:
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. View Student")
    print("5. Exit Student")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError as err:
        print(err)
        print("You did not enter a valid input")

    if choice == 1:
        system.add_student()
    elif choice == 2:
        system.delete_student()
    elif choice == 3:
        system.update_student
    elif choice == 4:
        system.view_student()
    elif choice == 5:
        break
    else: 
        print("Invalid Choice")
         


