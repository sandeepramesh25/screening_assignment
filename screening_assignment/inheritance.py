#Multiple Inheritance
class Human():
    def __init__(self,name):
        self.name = name

class Student():
    def __init__(self,age):
        self.age = age

class Skills(Human,Student):
    def __init__(self,name, age, skill):
        self.skills = skill
        Human.__init__(self, name)
        Student.__init__(self,age)


sandeep = Skills('sandeep',25,'dancer')
print("Name : {}, age : {}, skill : {}" .format(sandeep.name, sandeep.age, sandeep.skills))


