import random

# Parent class
class Person():
    '''Parent class, attributes will be inherited by subclasses'''
    def __init__(self, firstname, lastname, email, mobile):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.mobile = mobile

    def show_person(self):
        print("\nUser details:")
        print(f"\tFirstname: {self.firstname}")
        print(f"\tLastname: {self.lastname}")
        print(f"\tEmail: {self.email}")
        print(f"\tMobile: {self.mobile}")

# Student class
class Student(Person):
    '''Sub class of Person, additional attributes added to this class only'''
    def __init__(self, firstname, lastname, email, mobile, student_id, course):
        super().__init__(firstname, lastname, email, mobile)
        self.student_id = student_id
        self.course = course

    def show_student(self):
        self.show_person()
        print(f"\tStudent id: {self.student_id}")
        print(f"\tCourse: {self.course}\n")

    def add_student(self):
        print("Add student:")

# Teacher class
class Teacher(Person):
    '''Sub class of Person, additional attributes added to this class only'''
    def __init__(self, firstname, lastname, email, mobile, teacher_id, department):
        super().__init__(firstname, lastname, email, mobile)
        self.teacher_id = teacher_id
        self.department = department

    def show_teacher(self):
        self.show_person()
        print(f"\tTeacher id: {self.teacher_id}")
        print(f"\tDepartment: {self.department}\n")

    def add_teacher():
        print("Add teacher:")


def menu():
    '''Main menu, users will navigate to teacher db or student db'''
    while True:
        try:
            choice = int(input("Select options:\n" +
                               "1. show student\n" +
                               "2. show teacher\n" +
                               "3. exit\n"))

            if choice == 1:
                student()

            elif choice == 2:
                teacher()
            
            elif choice == 3:
                print("Goodbye")
                break
            break

        except ValueError:
            print("Incorrect option, try again")


def student():
    print("\n---------- Students Database --------------------\n")
    """This function is a navigation for students, user will be able taken to 3 different functions, add, view and return"""
    while True:
        try:
            choice = int(input("Select options:\n" +
                               "1. show student\n" +
                               "2. add student\n" +
                               "3. main menu\n"))

            if choice == 1:
                try:
                    new_student.show_student()
                except NameError:
                    print("No students found\n")

            elif choice == 2:
                add_student()

            elif choice == 3:
                print("Returning to main menu")
                print("\n---------- Main Menu ----------------------------\n")
                menu()
                break

        except ValueError:
            print("Incorrect option, try again\n")


def add_student():
    """In this function, user will input student details, this will then create an object called Student"""
    global new_student
    firstname = input("Enter firstname: ")
    lastname = input("Enter lastname: ")
    email = firstname + "." + lastname + "@student.com"
    while True:
        try:
            mobile = int(input("Enter mobile: "))
            break
        except ValueError:
            print("Enter mobile number again")
    course = input("Enter course: ")

    generator = random.randint(000000, 9999999)
    student_id = firstname[0].upper() + lastname[0].upper() + str(generator)

    print("Student added successfully")
    new_student = Student(firstname, lastname, email, mobile, student_id, course)
    student()


def teacher():
    """This function is a navigation for teachers, user will be able taken to 3 different functions, add, view and return"""
    print("\n---------- Teachers Database --------------------\n")
    while True:
        try:
            choice = int(input("Select options:\n" +
                                "1. show teacher\n" +
                                "2. add teacher\n" +
                                "3. main menu\n"))

            if choice == 1:
                try:
                    new_teacher.show_teacher()
                except NameError:
                    print("No teachers found\n")

            elif choice == 2:
                add_teacher()

            elif choice == 3:
                print("returning to main menu")
                print("\n---------- Main Menu ----------------------------\n")
                menu()
                break

        except ValueError:
            print("Incorrect option, try again\n")


def add_teacher():
    """In this function, user will input student details, this will then create an object called Teacher"""
    global new_teacher
    firstname = input("Enter firstname: ")
    lastname = input("Enter lastname: ")
    email = firstname + "." + lastname + "@student.com"
    while True:
        try:
            mobile = int(input("Enter mobile: "))
            break
        except ValueError:
            print("Enter mobile number again")
    department = input("Enter department: ")

    generator = random.randint(000000, 9999999)
    teacher_id = firstname[0].upper() + lastname[0].upper() + str(generator)

    print("Teacher added successfully")
    new_teacher = Teacher(firstname, lastname, email, mobile, teacher_id, department)
    teacher()


print("\n---------- Welcome ------------------------------\n")
menu()
