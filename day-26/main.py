import random

# numbers = [1, 2, 3]
# new_num = [n+1 for n in numbers]
# print(new_num)

students = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_names = [name.upper() for name in students if len(name) < 5]
# print(new_names)

students_score = {student: random.randint(1, 100) for student in students}
print(students_score)
passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
print(passed_students)
