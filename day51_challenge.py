# Codesaga Day 51
# Challenge: Student Portal

def menu():
    print("=== STUDENT PORTAL ===")
    print("1. View Profile")
    print("2. View Courses")
    print("3. View Attendance")
    print("4. Help")
    print("5. Exit")


def profile():
    print("Name: Laina")
    print("Roll: Student")
    print("Learning: Python")


def courses():
    print("Python")
    print("DSA")
    print("SQL Database")
    print("AI")


def attendance():
    print("Riya: Present")
    print("Rahul: Present")
    print("Laina: Present")


menu()
user = int(input("Choose option number: "))

while user != 5:

    if user == 1:
        profile()

    elif user == 2:
        courses()

    elif user == 3:
        attendance()

    elif user == 4:
        print("Read menu and try again!")

    else:
        print("Please choose correct option!")

    menu()
    user = int(input("Choose option number: "))