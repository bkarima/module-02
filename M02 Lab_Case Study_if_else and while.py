student_first_name = ""
student_last_name = ""
gpa = float


student_last_name = input("What is the student's last name? ")

if student_last_name == "ZZZ":
    print("Error, the last name you entered cannot be 'ZZZ'.  Please re-enter last name. ")


student_first_name = input("What is the student's first name? ")
print("Retrieving records for " + student_first_name + " " + student_last_name + ".  Please stand by...")

gpa = float(input("What is " + student_first_name + "'s GPA? "))

if gpa >= 3.5:
    print(student_first_name + " " + student_last_name + " is on the Dean's List.")
    
elif gpa >= 3.25:
    print(student_first_name + " " + student_last_name + " made the Honor Roll.")
    
else:
    print(student_first_name + " " + student_last_name + " did not make the Dean's List or the Honor Roll.")






