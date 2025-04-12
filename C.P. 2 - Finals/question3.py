from abc import ABC, abstractmethod

class School(ABC):
    def __init__(self, name, students):
        self.name = name
        self.students = students

    @abstractmethod
    def calculate_gpa(self):
        pass

    def display_grades(self):
        for student, grade in self.students.items():
            print(f"{student}: {grade}")

class SchoolOne(School):
    def calculate_gpa(self):
        avg = sum(self.students.values()) / len(self.students)
        return round(avg, 2)

class SchoolTwo(School):
    def calculate_gpa(self):
        total = sum(self.students.values())
        gpa = (total / (len(self.students) * 100)) * 4
        return round(gpa, 2)

def run_question3():
    students1 = {"Ana": 91, "Ben": 79, "Clara": 95}
    students2 = {"Dan": 85, "Ella": 81, "Finn": 93}

    s1 = SchoolOne("School One", students1)
    s2 = SchoolTwo("School Two", students2)

    print(f"{s1.name} GPA: {s1.calculate_gpa()}")
    print(f"{s2.name} GPA: {s2.calculate_gpa()}")
