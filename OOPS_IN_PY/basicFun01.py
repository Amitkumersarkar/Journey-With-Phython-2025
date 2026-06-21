class Student:
    name = ""
    Id = ""
    GPA = ""

    def set_value(self, Id, GPA):
        self.Id = Id
        self.GPA = GPA

    def display(self):

        print(f"Name : {self.name}, Id:{self.Id}, CGPA : {self.GPA}")


a = Student()
a.set_value(283, 3.02)
a.display()
