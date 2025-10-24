# Grade Calculator Program (Based on Total Marks)

# Input the number of subjects
num_subjects = int(input("Enter the number of subjects: "))

# Initialize total marks
total_marks = 0

# Input marks for each subject
for i in range(1, num_subjects + 1):
    marks = float(input(f"Enter marks for subject {i}: "))
    total_marks += marks

# Function to assign grade based on total marks
def assign_grade(total):
    if total >= 95:
        return "S"
    elif total >= 90:
        return "A+"
    elif total >= 80:
        return "A"
    elif total >= 70:
        return "B+"
    elif total >= 60:
        return "B"
    elif total >= 50:
        return "C"
    elif total >= 40:
        return "D"
    else:
        return "F"

# Get the grade
grade = assign_grade(total_marks)

# Print the results
print("\n--- Result ---")
print(f"Total Marks: {total_marks}")
print(f"Grade: {grade}")

