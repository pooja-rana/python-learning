class Person:
    def __init__(self, name, sex, profession):
        # data members (instance variables)
        self.name = name
        self.sex = sex
        self.profession = profession

    # Behavior (instance methods)
    def show(self):
        print('Name:', self.name, 'Sex:', self.sex, 'Profession:', self.profession)

    # Behavior (instance methods)
    def work(self):
        print(self.name, 'working as a', self.profession)

# create object of a class
per1 = Person('Jessa', 'Female', 'Software Engineer')

# call methods
per1.show()
per1.work()


#change attribute direct using obj
per1.name = "janvi"
per1.show()

#delete attribute

del per1.name
print(per1.name)

# output
# AttributeError: 'Person' object has no attribute 'name'

#delete object
per2 = Person('Jessa', 'Female', 'Software Engineer')
per2.show()

del per2

per2.work()

#output
# NameError: name 'per2' is not defined

