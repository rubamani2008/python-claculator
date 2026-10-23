# python -1
# Calculate the student grade,performance
name=input("Enter student name:")
n=int(input("Entee the number of subjects:"))
total=0
for i in range(1,n+1):
     mark=float(input(f"Enter for subject:{i}:"))
     total+=mark
     percentage=total/n
     if percentage>=90:
         grade="A+"
         performance="Outstanding"
     elif percentage>=80:
         grade="A"
         performance="Excellent"
     elif percentage>=70:
         grade="B"
         performance="Very Good"
     elif percentage>=60:
         grade="C"
         performance="Good"
     elif percentage>=50:
        grade="D"
        performance="Average"
     else:
        grade="F"
        performance="Need Improvement"
print("\n--- Acadamic Performance ---")
print("Student name:",name)
print("Total Marks:",total)
print("Percentage:",round(percentage,2),"%")
print("grade:",grade)
print("Performance:",performance)    
         
