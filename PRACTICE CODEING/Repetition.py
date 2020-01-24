# For condition tuple the repetition are proper apply and students are show three time in result.

students = ("John", "Jennie", "Jim", "Jack", "joe")
print(students)
print(type(students))
# 1. Repetition
students = ("John", "Jennie", "Jim", "Jack", "joe")
print(students)
print(type(students))
print(students*3)

# For condition list the repetition are proper apply and students are show three time in result.
students = ["John", "Jennie", "Jim", "Jack", "joe"]
print(students)
print(type(students))
# 1. Repetition
newStudents = students + ["Fionna", "George"]
print(newStudents)
print(students*3)


students = {"John", "Jennie", "Jim", "Jack", "joe"}
print(students)
print(type(students))
# 1. Repetition
newStudents = students + {"Fionna", "George"}       #   Error
print(newStudents)
print(students*3)
