echo 'def calculate_average(marks):
    return sum(marks) / len(marks)

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "D"

student_marks = [85, 92, 78, 90]
avg = calculate_average(student_marks)
grade = get_grade(avg)

print(f"Average: {avg}")
print(f"Grade: {grade}")' > grade_calculator.