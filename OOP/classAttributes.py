class Person:
    '''
    not specific to each ininstance of the class but for all class
    class attributes are used for constants, like gravity 
    '''
    number_of_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.add_person()
        Person.number_of_people += 1
    
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people()
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Krishna", 26)
p2 = Person("Prithvi", 24)


print(Person.number_of_people())
