"""
# Student class is defined with two different object
class student:

    def __init__(self, name, age, subject_1, subject_2, subject_3):
        self.name = name
        self.age = age
        self.sub1 = subject_1
        self.sub2 = subject_2
        self.sub3 = subject_3

    @staticmethod
    def marks(numb):
        res = numb
        print("The mark is", res)


s1 = student("vicky", 24, "Programming", "Database", "Algorithm")

print(s1.name)
print(s1.age)
print(s1.sub1)
print(s1.sub2)
s1.marks(90)

s2 = student("Jay", 25, "IoT", "Networking", "Python")
print(s2.name)
print(s2.age)
print(s2.sub1)
print(s2.sub2)
print(s2.sub3)
s2.marks(100)


# In class we have a function to display the results

class products:

    def __init__(self, name, description, price, rating):
        self.name = name
        self.des = description
        self.price = price
        self.rate = rating

    def display(self):
        print(self.name)
        print(self.des)
        print(self.price)
        print(self.rate)


p1 = products("Iphone", "This is Iphone X", 25000, [2, 3, 4, 5, 5])
p1.display()
p2 = products("Xi", "This is Xi 7", 23500, [2, 4, 3, 2, 5])
p2.display()
p3 = products("LENOVO", "This is LENOVO XE", 22900, [2, 5, 5, 2, 5])
p3.display()
"""
"""
# Encapsulation
class student:
    def __init__(self, id, name, std):
        self.__id = id
        self.__name = name
        self.__std = std

    def display(self):
        print(self.__id)
        print(self.__name)
        print(self.__std)
s1 = student(1, "Vicky", "XII")
s1.display()
s2 = student(2, "John", "XI")
# Alternative method to print the private variables
print(s2._student__id)
print(s2._student__name)
print(s2._student__std)
"""
"""
# Encapsualtion using Setter and Getter Method

class student:
    def setId(self,id):
        self.id = id
    def getId(self):
        print(self.id)

    def setName(self,name):
        self.name = name
    def getName(self):
        print(self.name)


s = student()
s.setId(100)
s.setName("vicky")
s.getId()
s.getName()

s1 = student()
s1.setId(101)
s1.setName("Peter")
s1.getId()
s1.getName()
"""
"""
#Inheritance

class dog:
    def __init__(self, speed, sound, behaviour):
        self.spd = speed
        self.sound = sound
        self.behav = behaviour

class GermanShepard(dog):
    def __init__(self, hair, height, speed, sound, behaviour):
        super().__init__(speed, sound, behaviour)
        self.hair = hair
        self.height = height

class Labrador(dog):
    def __init__(self, smart_level, speed, sound, behaviour):
        #Insted of using Parent class name and self (Dog.) we can use super()
        super().__init__(speed, sound, behaviour)
        self.smart = smart_level

d=dog("100KM","medium","good")
print(d.spd)
print(d.behav)
print(d.sound)

g = GermanShepard("more", "50", "100KM","medium","good")

print(g.hair)
print(g.height)

l = Labrador("High", "100KM","medium","good")
print(l.smart)
print("Lab", l.behav)

"""
"""
# Polymorphisom
class Dog:
    def __init__(self):
        pass

    def sound(self):
        print("BARK BARK")

class Cat:
    def __init__(self):
        pass

    def sound(self):
        print("Mewoooooooo")

def callTalk(obj):
    obj.sound()

d = Dog()
callTalk(d)
c = Cat()
callTalk(c)
"""
