class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value = value + student.get_grade()
        return value/len(self.students)
    
    
s1 = student("Prabin" , 21, 100)
s2 = student("Tim" , 21, 90)
s3 = student("Bill" , 22, 95)

course = course("Maths" , 3)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.get_average_grade())
print(course.students[2].name)
