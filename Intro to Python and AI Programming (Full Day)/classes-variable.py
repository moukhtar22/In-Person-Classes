class Person:
    def __init__(self, name,age,size):
        self.name = name
        self.age = age
        self.size = size

student = Person('bob',11,'large')

print(student)
print(vars(student))
print(student.name)
print(student.age)
print(student.size)
