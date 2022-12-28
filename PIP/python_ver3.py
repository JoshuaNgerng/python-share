#ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、
#｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ
#ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀
#｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ
#｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ
#ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、
#｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ
#ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀
#｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ
#｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ

# printout main menu
def menu():
    print("*********** Main Menu ************\n")
    print("1. Add Student Record\n")
    print("2. Update Student Record\n")
    print("3. View Student Record\n")
    print("4. Search Student Record\n")
    print("5. Display Highest and Lowest Grade\n")
    print("6. Exit\n")

# print out minimenu for option 2
def menu2():
    print("*** Update Student Record Menu ***\n")
    print("1. Update Student Grade\n")
    print("2. Delete Student Entry\n")
    print("3. Return to Main Menu\n")

# prompt user to choose their options
# and confirms their choice
def reponse():
    global option
    global confirm
    option = str(input("Enter your choice: "))
    confirm = str(input("Your choice is %s Are you sure you want to continue? Y/N " %option))
    while confirm != 'Y' and confirm != 'N':
        confirm = str(input("Your choice is %s Are you sure you want to continue? Y/N " %option))

# different messages to prompt the user 
# base on bool given
def msg(name, bool):
    if bool == 0:
        return("\nError acessing database\nTo create a database use option 1 in main menu")
    elif bool == 1:
        return(f"\n{name}'s record have been deleted")
    elif bool == 2:
        return(f"\n{name}'s record have been updated")
    elif bool == 3:
        return(f"\n{name}'s record cannot be found")
    else:
        return("\nDatabase is empty")

# take input from user
# then check whether it is a validate name
def in_name():
    global name
    name = str(input("Enter Student name: "))
    i = 1
    while i != 0:
        for index in name:
            if (index >= 'A' and index <= 'Z') or (index >= 'a' and index <= 'z') or index == ' ':
                i = 0
            else:
                i = 1
                print("A name must contain only characthers or space")
                break
        if i == 0 and index == " ":
            i = 1
            print("A name cannot end with spaces")
        if i == 1:
            name = str(input("Enter Student name: "))

# convert the string input into an integer
# if all characters in string are numbers
def ft_atoi(str):
    if not str:
        return (-1)
    for index in str:
        if (index >= '0' and index <= '9'):
            x = 0
        else:
            x = 1
            break
    if x == 0:
        total = int(str)
        return(total)
    else:
        return(-1)

# validate different grades base on bool given
# bool = 1 is assignment
# bool = 2 is mid-test
# bool = 3 is final exam
def valid_grade(bool, grade):
    global prompt
    bool = int(bool)
    grade = int(grade)
    if bool == 1:
        max = int(30)
        prompt = "assignment"
    elif bool == 2:
        max = int(20)
        prompt = "mid-test"
    else:
        max = int(50)
        prompt = "final exam"
    x = 0
    while x != 1:
        if grade >= 0 and grade <= max:
            x = 1
        else:
            x = 0
            if grade == -1:
                print("Grade must be only numbers")
            else:
                print(f"The {prompt} grade must be 0 - {max}")
            grade = ft_atoi(input(f"Enter {prompt} grade: "))
    return(grade)

# take input from user and validity if it is a valid grade   
def in_grade():
    global grade1
    global grade2
    global grade3
    grade1 = ft_atoi(input("Enter assignment grade: "))
    grade1 = valid_grade(1, grade1)
    grade2 = ft_atoi(input("Enter mid-test grade: "))
    grade2 = valid_grade(2, grade2)
    grade3 = ft_atoi(input("Enter final exam grade: "))
    grade3 = valid_grade(3, grade3)

# define the output to be written into the database
def output(name, grade1, grade2, grade3):
    total = int(grade1) + int(grade2) + int(grade3)
    if total >= 80 and total <= 100:
        grade = str("A+")
    elif total >= 75 and total <= 79:
        grade = str("A")
    elif total >= 70 and total <= 74:
        grade = str("B+")
    elif total >= 65 and total <= 69:
        grade = str("B")
    elif total >= 60 and total <= 64:
        grade = str("C+")
    elif total >= 55 and total <= 59:
        grade = str("C")
    elif total >= 50 and total <= 54:
        grade = str("C-")
    elif total >= 40 and total <= 49:
        grade = str("D")
    elif total >= 30 and total <= 39:
        grade = str("F+")
    elif total >= 20 and total <= 29:
        grade = str("F")
    else:
        grade = str("F-")
    return(f"{name}:{grade1}.{grade2}.{grade3},{total}:{grade}\n")

# set index of string to grade
def index_grade(line):
    i = 0
    while line[i] != ",":
        i += 1
    i += 1
    return(i)

# fetch name or grade from data for if condition
def fetch_data(line, i):
    out = ""
    while line[i] != ":" and line[i] != '\n':
        out += line[i]
        i += 1
    i += 1
    return(out)

# get grade from database
def fetch_grade(line):
    i = index_grade(line)
    out = int(0)
    while line[i] >= "0" and line[i] <= "9":
        out = out * 10 + int(line[i])
        i += 1
    return(out)

# bool = 1 get highest grade
# bool = 2 get lowest grade
def sort_grade(bool, lines):
    global ref
    global index
    ref = fetch_grade(lines[0])
    for line in lines:
        index = fetch_grade(line)
        if bool == 1:
            if index > ref:
                ref = index
        if bool == 2:
            if index < ref:
                ref = index
    return(ref)

# read student records from database
# and edit different entry in database
# base on the bool given
def read_write_data(bool, name, out):
    global ref
    counter = 0
    with open('Database.txt', 'r') as data:
        lines = data.readlines()
        data.close()
        with open('Database.txt', 'w') as new:
            for line in lines:
                ref = fetch_data(line, 0)
                if ref != name:
                    new.write(line)
                else:
                    counter += 1
                    if bool == 2:
                        new.write(out)
    if counter == 0:
        print(msg(name, 3))
    else:
        print(msg(name, bool))
    new.close()

# read student records from database
# then print out different entry 
# base on the bool given
def read_data(bool, input):
    global ref
    global i
    out = []
    counter = 0
    with open('Database.txt', 'r') as data:
        lines = data.readlines()
        if bool == 4:
            out = lines
            counter = 1
        else:
            for line in lines:
                if bool == 3:
                    ref = fetch_data(line, 0)
                if bool == 5:
                    i = index_grade(line)
                    ref = fetch_data(line, i)
                if ref == str(input):
                    out.append(line)
                    counter += 1
    if counter == 0:
        print(msg(input, bool))
    else:
        print()
        print_table(out)
    data.close()

# determine the width for the first column
def find_max_len(lines):
    max_len = int(12)
    for line in lines:
        i = int(0)
        while(line[i] != ":"):
            i += 1
            if (i > max_len):
                max_len = i
    return(max_len)

# print the outline of the table
def print_outer(max_len, char):
    out = "+"
    i = int(0)
    while i < max_len + 3:
        if char == "=":
            out += "="
        if char == "-":
            out += "-"
        i += 1
    if char == "=":
        out += "+==============+============+==============+==============+"
    if char == "-":
        out += "+--------------+------------+--------------+--------------+"
    print(out)

# print out the header for the table
def print_header(max_len):
    out = "| Student name"
    i = 0
    while i < max_len + 3 - 13:
        out += " "
        i += 1
    out += "|  Assignment  |  Mid-test  |  Final Exam  |    Grade     |"
    print(out)

# sort the amount of spaces required 
# to print out the proper width
def sort_print(ref_len, input):
    l = len(input)
    i = 0
    out = ""
    while i < ref_len - l:
        out += " "
        i += 1
    return(out)

# retrieved information from database to print
def loop_str(line, i, key):
    out = ""
    while line[i] != key and line[i] != '\n':
        out += line[i]
        i += 1
    i += 1
    return(out, i)

# organize the student records into a table
def sp_print(line, max_len):
    i = 0
    name, i = loop_str(line, i, ":")
    score1, i = loop_str(line, i, ".")
    score2, i = loop_str(line, i, ".")
    score3, i = loop_str(line, i, ",")
    total, i = loop_str(line, i, ":")
    grade, i = loop_str(line, i, "\n")
    ref_len = max_len + 2
    out = f"| {name}"
    out += sort_print(ref_len, name)
    out += f"|      {score1}"
    out += sort_print(8, score1)
    out += f"|     {score2}"
    out += sort_print(7, score2)
    out += f"|      {score3}"
    out += sort_print(8, score3)
    out += f"|  {total}"
    out += sort_print(5, total)
    out += f"|  {grade}"
    out += sort_print(4, grade) + "|"
    print(out)

# organize the output into a table and print it out
def print_table(lines):
    max_len = find_max_len(lines)
    print_outer(max_len, "=")
    print_header(max_len)
    print_outer(max_len, "=")
    for line in lines:
        sp_print(line, max_len)
        print_outer(max_len, "-")

# check whether the input name already exist in the record
def check_unique(name):
    try:
        with open('Database.txt', 'r') as data:
            lines = data.readlines()
            data.close()
            for line in lines:
                ref = fetch_data(line, 0)
                if ref == name:
                    print(f"{name}'s record already exist")
                    return(-1)
        return(0)
    except:
        print("No Database, creating new database")
        return(0)

# add a student's record 
def addStudent():
    global i
    in_name()
    i = check_unique(name)
    while i != 0:
        in_name()
        i = check_unique(name)
    in_grade()
    out = output(name, grade1, grade2, grade3)
    try:
        with open('Database.txt', 'a') as data:
            data.write(out)
        data.close()
        print(f"\nSuccessfully added {name}'s record")
    except:
        print("Database cannot be accessed nor created")

# delete a student's record
def deleteStudent():
    in_name()
    try:
        read_write_data(1, name, "\0")
    except:
        print(msg("\0", 0))

# display the record of a student that user input
def searchStudent():
    in_name()
    try:
        read_data(3, name)
    except:
        print(msg("\0", 0))

# update the grades of existing students
def updateStudentGrade():
    in_name()
    in_grade()
    out = output(name, grade1, grade2, grade3)
    try:
        read_write_data(2, name, out)
    except:
        print(msg("\0", 0))

# display all student in record
def viewAllStudents():
    try:
        read_data(4, "\0")
    except:
        print(msg("\0", 0))

# display the students with highest and lowest grade
def displayHighestLowestGrade():
    global high
    global low
    try:
        with open('Database.txt', 'r') as data:
            lines = data.readlines()
            high = sort_grade(1, lines)
            low = sort_grade(2, lines)
            print()
            print("The highest grade is: ")
            read_data(5, high)
            print()
            print("The lowest grade is: ")
            read_data(5, low)
            data.close()
    except:
        print(msg("\0", 0))

# menu option for user to choose to 
# update or delete student record under option 2
def minimenu():
    print()
    menu2()
    reponse()
    while option != '3' or confirm != 'Y':
        if confirm == 'Y':
            if option == '1':
                updateStudentGrade()
            elif option == '2':
                deleteStudent()
            else:
                print('Invalid option.')
        print()
        menu2()
        reponse()

# main function

# take inputs from user
menu()
reponse()
# while loop to repeat menu and perform different options
# exit program only if user input 6, then Y
while option != '6' or confirm != 'Y':
    if confirm == 'Y':
        if option == '1':
            addStudent()
        elif option == '2':
            minimenu()
        elif option == '3':
            viewAllStudents()
        elif option == '4':
            searchStudent()
        elif option == '5':
            displayHighestLowestGrade()
        else:
            print('Invalid option.')
    # take inputs from user
    print()
    menu()
    reponse()
print("Thank you for using the program. Have a great day")

#ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、
#｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ
#ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀
#｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ
#｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ
#ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、
#｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ
#ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀
#｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ
#｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、｀、ヽヽ｀ヽ｀、ヽヽ｀ヽ｀、ヽヽ