class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [
    Student("Hassan", 78),
    Student("Ali", 45),
    Student("Sara", 92),
]

def top_scorer(student_list):
    if not student_list:
        raise ValueError("student_list cannot be empty.")
    return max(student_list, key=lambda student: student.score)

print("Students who passed:")
for student in students:
    if student.score > 50:
        print(student.name, "-", student.score)

best_student = top_scorer(students)
print("\nTop scorer:")
print(best_student.name, "-", best_student.score)
