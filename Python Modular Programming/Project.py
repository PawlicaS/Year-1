# Szymon Pawlica R00187226
import reading_from_user


def read_data():
    connection = open("login_details.txt")
    # get the password and username from the .txt
    uname_list = []
    pass_list = []
    lines = connection.readlines()
    uname_list.append(lines[0].rstrip())
    pass_list.append(lines[1].rstrip())
    # return the username and password in two lists
    return uname_list, pass_list


def valid_check(uname_list, pass_list, name, password):
    # check if the given username and password match those in the lists
    if name in uname_list:
        i = uname_list.index(name)
        if password == pass_list[i]:
            print(f"Welcome {name}")
        else:
            print("\nModule Record System: Login Failed.")
            exit()
    else:
        print("\nModule Record System: Login Failed.")
        exit()


def menu():
    print(f"\nModule Record System - Options"
          f"\n=============================="
          f"\n\t1. Record Attendance"
          f"\n\t2. Generate Statistics"
          f"\n\t3. Exit")
    menu_choice = reading_from_user.read_range_integer(">", 1, 3)
    if menu_choice == 1:
        record_attendance()
    elif menu_choice == 2:
        generate_statistics()
    else:
        exit()


def generate_statistics():
    print(f"\nModule Record System (Statistics) - Choose a Module"
          f"\n===================================================")
    # get module from modules function
    module = modules_list()
    # let module = the name of the module
    if module == 1:
        module = "SOFT_6017"
    else:
        module = "SOFT_6018"
    print(f"\nModule Record System(Statistics) {module}"
          f"\n==========================================")
    # get student data from student data function
    names, present_list, absent_list, excused_list = student_data(module)
    # get data required for the statistics
    no_of_students = len(names)
    no_of_classes = int(present_list[0]) + int(absent_list[0]) + int(excused_list[0])
    non_attenders = []
    best_attenders = []
    low_attenders = []
    i = 0
    attendance = 0
    best_attendance = 0
    while i < no_of_students:
        attendance = attendance + int(present_list[i])
        if int(present_list[i]) == 0:
            non_attenders.append(names[i])
        if int(present_list[i]) >= 1:
            if float(present_list[i]) / float(no_of_classes) <= .7:
                low_attenders.append(names[i])
        if int(present_list[i]) >= best_attendance:
            best_attendance = int(present_list[i])
        i = i + 1
    i = 0
    while i < no_of_students:
        if int(present_list[i]) == best_attendance:
            best_attenders.append(names[i])
        i = i + 1
    avg_attendance = attendance / no_of_students
    print(f"Module: {module}\n"
          f"Number of Students: {no_of_students}\n"
          f"Number of Classes: {no_of_classes}\n"
          f"Average Attendance: {avg_attendance:.1f}\n"
          f"Low Attender(s): under 70%")
    i = 0
    while i < len(low_attenders):
        print(f"\t{low_attenders[i]}")
        i = i + 1
    print(f"Non Attender(s):")
    i = 0
    while i < len(non_attenders):
        print(f"\t{non_attenders[i]}")
        i = i + 1
    print(f"Best Attender(s):\n"
          f"\tAttended {best_attendance}/{no_of_classes} days")
    i = 0
    while i < len(best_attenders):
        print(f"\t{best_attenders[i]}")
        i = i + 1


def record_attendance():
    print(f"\nModule Record System (Attendance) - Choose a Module"
          f"\n===================================================")
    # get module from modules function
    module = modules_list()
    # let module = the name of the module
    if module == 1:
        module = "SOFT_6017"
    else:
        module = "SOFT_6018"
    print(f"\nModule Record System(Attendance) {module}"
          f"\n==========================================")
    # get student data from student data function
    names, present_list, absent_list, excused_list = student_data(module)
    print(f"There are {len(names)} students enrolled")
    i = 0
    # input attendance for students in module
    while i < len(names):
        print(f"\nStudent #{i + 1}: {names[i]}"
              f"\n1. Present"
              f"\n2. Absent"
              f"\n3. Excused")
        attendance = reading_from_user.read_range_integer(">", 1, 3)
        if attendance == 1:
            value = present_list.pop(i)
            value = int(value) + 1
            value = str(value)
            present_list.insert(i, value)
        elif attendance == 2:
            value = absent_list.pop(i)
            value = int(value) + 1
            value = str(value)
            absent_list.insert(i, value)
        else:
            value = excused_list.pop(i)
            value = int(value) + 1
            value = str(value)
            excused_list.insert(i, value + "\n")
        i = i + 1
    # clear the module .txt
    clear = open(module + ".txt", "w+")
    clear.write("")
    clear.close()
    i = 0
    # append onto the empty module .txt
    connection = open(module + ".txt", "a+")
    while i < len(names):
        connection.write(f"{names[i]},{present_list[i]},{absent_list[i]},{excused_list[i]}")
        i = i + 1
    connection.close()
    print(f"{module}.txt updated with latest attendance records")


def modules_list():
    comma = ","
    dash = " -"
    connection = open("modules.txt")
    lines = connection.readlines()
    modules_list = [x.strip() for x in lines]
    # change the "," into a "-" and enumerate the list
    for i, module in enumerate(modules_list):
        print(f"\t{i + 1}. {module.replace(comma, dash)}")
    # return the module chosen
    module_choice = reading_from_user.read_range_integer(">", 1, len(modules_list))
    return module_choice


def student_data(module):
    # record student data (name, days present, absent and excused)
    connection = open(module + ".txt")
    names = []
    present_list = []
    absent_list = []
    excused_list = []
    while True:
        line = connection.readline()
        if line == "":
            break
        line_data = line.split(",")
        names.append(line_data[0])
        present_list.append(line_data[1])
        absent_list.append(line_data[2])
        excused_list.append(line_data[3])
    # return the lists
    return names, present_list, absent_list, excused_list


def main():
    uname_list, pass_list = read_data()
    print("\nModule Record System"
          "\n====================")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    valid_check(uname_list, pass_list, username, password)
    # keep running the menu until exit
    while True:
        menu()


main()
