student_percentage: int = int(input("Enter your percentage: "))


if student_percentage >= 90:
    print("Your Grade: +A")
elif student_percentage >= 80:
    print("Your Grade: A")
elif student_percentage >= 70:
    print("Your Grade: B")
elif student_percentage >= 60:
    print("Your Grade: C")
elif student_percentage >= 50:
    print("Your Grade: D")
else:
    print("Your Are Fail")