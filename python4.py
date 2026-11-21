import csv
students=[
    {"RollNO":"101","Name":"Anitha","Department":"CSE","Mark":86},
    {"ROLL NO":"103","Name":"Bala","Department":"CSE","Mark":91},
    {"ROLL NO":"103","Name":"Chitra","Department":"ECE","Mark":78}
]
couse=("Python",4)
print("Course tuple:",course)
with open("Students.txt","w")as file:
    for student in students:
        file.write(str(student)+"\n")
        with open("Student.csv","w",newline="")as file:
            fileds=["RollNO","Name","Department","Mark"]
            writer=csv.DictWriter(file,fieldnames=fields)
            writer.writerheader()
            writer.writerows(students)
            print("\n---Records form CSV---")
            with open("Students.csv","r")as file:
                reader=csv.DictReader(file)
                for row in reader:
                    print(row["ROLLNO"],row["Name"],row["Department"],row["Mark"])