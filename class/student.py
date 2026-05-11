class Student:
    
    def __init__(self, nameStudent, lastnameStudent, age, course):
        self.nameStudent = nameStudent
        self.lastnameStudent = lastnameStudent
        self.age = age
        self.course = course

    def __str__(self):
        return f"{self.nameStudent} {self.lastnameStudent}, {self.age} лет, курс: {self.course}"
