# creating class
class Student:
    name = ""
    id = ""
    cgpa = ""


# creating object
obj = Student()
print(isinstance(obj, Student))
obj.name = "Amit"
obj.id = 283
obj.cgpa = 3.02
print(f"Name : {obj.name}, Id:{obj.id}, CGPA : {obj.cgpa}")
