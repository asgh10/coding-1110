student = {
    "name": "현빈",
    "age": 17,
    "major": "소프트웨어개발과"
}

def print_student(student):
    print(f"학생 이름: {student["name"]} \n학생 나이: {student["age"]} \n학생 직업: {student["major"]}")

print_student(student)

def update_age(student, new_age):
    student["age"] = new_age
    print(f"학생 이름: {student['name']} \n변경된 나이: {student['age']}")

update_age(student, 18)

def update_major(student, new_major):
    student['major'] = new_major
    print(f"학생 이름: {student['name']} \n변경된 전공: {student['major']}")

update_major(student, "백엔드 개발자")

def update_student(student, new_age, new_major):
    student['age'] = new_age
    student['major'] = new_major
    print(f"학생 이름: {student['name']} \n나이: {student['age']} \n전공: {student['major']}")

update_student(student, 19, "백엔드 개발자")