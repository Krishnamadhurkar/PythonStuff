# This is to revise OOP concepts in Python 
'''
The best way to learn programming is by practicing, so lets do it lol:
Golden Rules to follow:

'''


'''
Create my own class

name class use uppercase letter camelcase 
'''

class Dog:
    # def meow(self):
    #     print("meow")
    def __init__(self, name, age):
        self.name = name # attribute of class Dog called name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def set_age(self,age):
        self.age = age

    def add_one(self, x):
        return x+1

    def bark(self):
        print("bark")

d = Dog("Tim",4)
print(d.name)
d2 = Dog("Gizmo",9)
print(d2.name)
print(d2.age)
print(d2.get_age()) 
d2.set_age(10)
print(d2.get_age())

print(d.add_one(2))
print(type(d))