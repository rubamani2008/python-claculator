students={}
def add_student():
    roll=input("Enter the roll no:")
    name=input("Enter the name")
    dept=input("Ente the department:")
    students[roll]={"Name":name,"Department":dept}
    print("Student added sucessfully.")
def view_students():
    if not students:
        print("No of student records founded")
        return
    print("\n--Student Records--")
for roll,data in students.items():
      print("Roll NO:",roll,"|Name:",data["Name"],
            "|Department:",data["Department"])
def search_student():
    roll=input("Enter the roll no to search:")
    if roll in students:
        print(students[roll])
    else:
        print("Student not found.")
def delete_student():
    roll=input("Enter roll no to delete:")
    if roll in students:
        del students[roll]
        print("Student deleted sucessfully")
    else:
        print("Stdents not founded")
    while True:
        print("\n1. Add student")
        print("2.view students")
        print("3.search student")
        print("4.Delete student")
        print("5.exit")
        choice=input("enter your choice:")
        if choice=="1":
            add_student()
        elif choice=="2":
            view_students()
        elif choice=="3":
            search_student()
        elif choice=="4":
            delete_student()
        elif choice=="5":
            print("Exiting...")
            break
        else:
            print("Invalid choice")