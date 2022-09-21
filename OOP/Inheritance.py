'''
Pet 

cat, dog etc inherit from the pet class and methods in these classes are to be defined that are different 
between cat dog classes eg: speak

In a gist Make class that defines main attributes and then subclasses that do things differently than each other 
ex: person class has name age etc but employee and manager class have a few thing that both cannot do 
'''

class Pet:
    def __init__(self, name, age):
        self.name = name # attribute of class Dog called name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("i dont know what to say")




class Dog(Pet):
    def speak(self):
        print("Bark")

class Cat(Pet):
    def __init__(self, name, age, color):
        '''
        Use super to pass sub class through super class initialization 
        and then continue to sub class initialization, like we want cat object to first get the name and age 
        defined from pet super class and then color from the cat class
        Important for setting up objects correctly 
        '''
        super().__init__(name,age) 
        self.color = color

    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Fish(Pet):
    pass


p = Pet("Tim", 19)
p.show()
c = Cat("Pounce", 10, "Gray")
c.show()
f =Fish("Goldie",2)
f.speak()
c.show