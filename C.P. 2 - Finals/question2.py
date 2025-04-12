class Employee:
    def __init__(self, name, age=None, department="General"):
        self.__name = name  # Encapsulation
        self.__age = age
        self.__department = department

    @classmethod
    def from_string(cls, emp_str):
        name, age, dept = emp_str.split("-")
        return cls(name, int(age), dept)

    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}, Department: {self.__department}")

def run_question2():
    emp1 = Employee("Sophia", 26, "HR")
    emp2 = Employee.from_string("Gerald-31-IT")
    emp1.display_info()
    emp2.display_info()
