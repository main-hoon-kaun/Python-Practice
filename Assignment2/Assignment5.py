marks=float(input("Enter the student's marks(0 to 100): "))
if marks < 0 or marks >100:
    print("Invalid marks entered. Please enter a value between 0 and 100.")
else:
    if marks>=90:
        grade="Grade A"
    elif marks>=80:
        grade="Grade B"
    elif marks>=70:
        grade="Grade C"
    elif marks>=60:
        grade="Grade D"
    else:
        grade="Fail"

    print(f"The student scored {marks} and received: {grade}")
