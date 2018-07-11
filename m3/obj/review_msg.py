class Teacher:
    salary = 1000

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def course(self):
        Teacher.salary -= 50
        print('coursed')

class Student():
    salary = 1000

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def course(self):
        Student.salary -= 50
        print('coursed')

t = Teacher('alex',12)
s = Student('peiqi',15)

t.course()
s.course()
print(t.salary)
print(s.salary)


