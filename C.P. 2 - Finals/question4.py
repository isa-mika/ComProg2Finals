class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __add__(self, other):
        return Vector(self.__x + other.__x, self.__y + other.__y)

    def __str__(self):
        return f"Vector({self.__x}, {self.__y})"

def run_question4():
    v1 = Vector(3, 4)
    v2 = Vector(5, 2)
    result = v1 + v2
    print("Result of Vector Addition:", result)
