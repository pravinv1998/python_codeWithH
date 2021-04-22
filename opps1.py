
class Student():
    def __init__(self, sname, sage, srole):
        self.name = sname
        self.age = sage
        self.role = srole

    def stud_details(self):
        print(f"name is {self.name} , age = {self.age} , and also role of the student is {self.role}")

name = input("Enter name: ")
age = int(input("Insert Age: "))
role = input("Insert role: ")

pravin = Student(name, age, role)

print(pravin.stud_details())