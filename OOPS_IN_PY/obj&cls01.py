class Student:
    # name = "Amit"

    def __init__(self, fullName):  # constructor
        self.name = fullName
        print("adding new student in DB")


s1 = Student("Amit")
print(s1.name)
