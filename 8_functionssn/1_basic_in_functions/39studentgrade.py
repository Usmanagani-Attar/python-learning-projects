def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

marks = float(input("Enter the student's marks: "))
grade = calculate_grade(marks)
print(f"The grade is: {grade}")
