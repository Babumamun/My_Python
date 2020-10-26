all_students=[] #global variable will store all studnts data
def chose_option():
    print("\n------- Welcome to Neusoft University Student Management System ------\n")
    print('A: Add Students')
    print('L: List all students')
    print('D: Delete student')
    print('S: Search student')
    print('U: Update Student list')
    print('Q: Quit')

def interact_with_option():
    chose_option()
    while True:
        try:
            user_input = input("Enter a choice:A/L/D/S/U/Q:")
            if user_input.isdigit():
                raise Exception
            elif user_input.upper()=="A":
                add_students()
            elif user_input.upper()=="L":
               student_list()
            elif user_input.upper()=="D":
                delete_student()
            elif user_input.upper() == "S":
                search_student()
            elif user_input.upper() == "U":
                update_student()
            elif user_input.upper() == "Q":
                quit()
        except Exception as e:
            print("invalid Input !Please input a capital letter!")


def add_students():
    while True:
        try:
            roll_num=int(input("Enter a roll number of the student:"))
            stu_name=input("Enter a Name of the student:")
            stu_age=int(input("Enter age number of the student:"))
        except ValueError as g:
            print("invalid Input !Please input digit!")
        else:
            break
    chec_duplicate=[student for student in all_students if student [0] == roll_num]
    if chec_duplicate ==[]:
        new_student=[roll_num,stu_name,stu_age]
        all_students.append(new_student)
        print("Student successfully added!")
    else:
        print("This RollNumber is not available!")
        tryAgain()
def student_list():
    print(all_students)
    tryAgain()

def delete_student():
    try:
        id=int(input("Please Enter Student RollNumber to delete"))
        for stu in all_students:
            if id in stu:
                all_students.remove(stu)
                print("The Student Info was deleted successfully")
    except ValueError:
        print("invalid Input !Please input digit!")

def search_student():
    try:
        id = int(input("Please Enter Student RollNumber to Search:"))
        for stu in all_students:
            if id in stu:
                print(stu)
    except ValueError:
        print("invalid Input !Please input digit!")
        tryAgain()

def update_student():
    try:
        id = int(input("Please Enter Student RollNumber to Update:"))
        for student in all_students:
            if id in student:
                print("Do u want update this student?" +str(student))
                option = input("yes/no\n")
                if option.upper() == "YES":
                    for stu in all_students:
                        if id in stu:
                            all_students.remove(stu)
                    roll_num = int(input("Enter Update roll number "))
                    stu_name = input("Enter Update  Name:")
                    stu_age = int(input("Enter Update age:"))
                    update_student = [roll_num, stu_name, stu_age]
                    all_students.append(update_student)
                    print("Student Update successfully!")
                    print("Here is updated student Inf"+str(update_student))
                    tryAgain()
                else:
                    exit()
            if id not in student:
                print("Student was not found")
    except ValueError:
        print("invalid Input !Please input digit!")
        tryAgain()





def tryAgain():
    user_input = input("Do You want to Try again?Yes/No\n")
    if user_input.upper() == "YES":
        interact_with_option()
    else:
        quit()


interact_with_option()







