# Student Grading System

def calculate_grade(score):
    if score >= 90:
        return 'A+'
    elif score >= 80:
        return 'A'
    elif score >= 75:
        return 'B+'
    elif score >= 70:
        return 'B'
    elif score >= 65:
        return 'C+'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'  
while True:
    try:
        score = float(input("Enter the student's score (0-100): "))
        if 0 <= score <= 100:
            grade = calculate_grade(score)
            print(f"The student's grade is: {grade}")
        else:
            print("Please enter a valid score between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    
    next_student = input("Do you want to enter another student's score? (yes/no): ")
    if next_student.lower() == "no":
        break
