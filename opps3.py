class Employee():
    no_of_leaves = 10
    def __init__(self, st_name, st_age, st_role):
        self.name = st_name
        self.age = st_age
        self.role = st_role

    def st_details(self):
        print(f" name {self.name}, age {self.age}, role is {self.role}")

    @classmethod
    def change_leaves_value(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    def write_file(self):
        value = open("data.txt","a")
        value.write("Name is "+self.name+" Age: "+self.age+" Role is "+self.role+"\n")
        value.close()
        # value.write(self.age)
        # value.write(self.role)
        # value.write("========================================================")

    @classmethod
    def from_str(cls, str):
        params = str.split(" ")
        return cls(params[0],params[1], params[2])



name = input("Name: ")
# age = input("Age: ")
# role = input("Role: ")

pravin = Employee.from_str(name)
# pravin = Employee(name,age,role)
# pravin.change_leaves_value(15)
# print(pravin.st_details()," ", pravin.no_of_leaves)

print(pravin.write_file())
