from operator import itemgetter, attrgetter

students = [
    ("jane", 22, "A"),
    ("dave", 32, "B"),
    ("sally", 17, "B"),
]

result = sorted(students, key=itemgetter(1))
print(result)

studens = [
    {"name": "jane", "age": 22, "grade": "A"},
    {"name": "dave", "age": 32, "grade": "B"},
    {"name": "sally", "age": 17, "grade": "B"},
]

result = sorted(studens, key=itemgetter("age"))
print(result)


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


students = [
    Student("jane", 22, "A"),
    Student("dave", 32, "B"),
    Student("sally", 17, "B"),
]

result = sorted(students, key=attrgetter("age"))
print(result)
