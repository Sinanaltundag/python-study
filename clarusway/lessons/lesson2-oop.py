# oop

import os
os.system("cls" if os.name == "nt" else "clear")

""" def print_type(data):
    for i in data:
        print(i, type(i))

test = [122, "sinan", [1,2,3], (3,5,7), True, lambda x:x]
print_type(test) """

# class Person:
#     name = "sinan"
#     age = 40

# person1 = Person()
# person2 = Person()

# print(person1.name)
# print(person2.name)

# Person.job = "developer"

# person1.location = "Turkey"
# print(person2.location)

# class Person:
#     name = "sinan"
#     age = 40
#     def test(self):
#         print("test")
    
#     def set_details(self, name, age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(self.name, self.age)

# person1 = Person()
# person1.test()

# person1.set_details("ali", 20)
# person1.get_details()

# person2 = Person()
# person2.get_details()

# class Person:
#     company = "Clarusway"

    
#     def test(self):
#         print("test")
    
#     def set_details(self, name, age):
#         self.name = name
#         self.age = age

#     def get_details(self):
#         print(self.name, self.age)
    
#     @staticmethod
#     def salute():
#         print("Hi welcome")

# person1 = Person()
# person1.salute()

# special methods
""" class Person:
    company = "Clarusway"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

    def get_details(self):
        print(self.name, self.age)

person1 = Person("sinan", 40)

person1.get_details()

liste = [4,2,6,9,0]
print(liste)
print(person1) """

""" class Person:
    company = "Clarusway"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._id = 5000 # _ değiştirmeyin anlamına geliyor ama değişiyor
        self.__id = 6000 # __ değiştirmeyin anlamına geliyor yine ve dolambaçlı değiştirilebiliyor

    def __str__(self):
        return f"{self.name} {self.age}"

    def get_details(self):
        print(self.name, self.age)

person1= Person("deneme", 20)

print(person1._id)
# print(person1.__id)   çalışmaz
print(person1._Person__id) """


class Person:
    company = "Clarusway"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._id = 5000 # _ değiştirmeyin anlamına geliyor ama değişiyor
        self.__id = 6000 # __ değiştirmeyin anlamına geliyor yine ve dolambaçlı değiştirilebiliyor

    def __str__(self):
        return f"{self.name} {self.age}"

    def get_details(self):
        print(self.name, self.age)

class Lang:
    def __init__(self, langs):
        self.langs = langs





class Lang:
    def __init__(self,langs):
        self.langs = langs

    def display_langs(self):
        print(self.langs)

class Employee(Person, Lang):
    def __init__(self, name, age, path, langs):
        # self.name = name
        # self.age = age
        super().__init__(name,age)
        self.path = path
        Lang.__init__(self, langs)
        # self.langs = langs

    # override
    def get_details(self):
        # print(self.name, self.age, self.path)
        super().get_details()
        print(self.path)

emp1 = Employee("hamza", 30, "Fullstack", ["python", "js"])
emp1.get_details()
emp1.display_langs()

print(Employee.mro())

Person.name = "deneme"

print(emp1)
emp2= Employee("aaa", 30, "Fullstack", ["python", "jsx"])