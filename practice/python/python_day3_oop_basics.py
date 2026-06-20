# Python Day 3 — OOP Basics

# A class is a blueprint for creating objects
# __init__ runs automatically when an object is created
# self refers to the current object being worked with

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount


# Creating objects (instances) from the class
e1 = Employee("Rahul", 40000)
e1.give_raise(5000)
print(e1.salary)   # 45000

e2 = Employee("Sakshi", 50000)
print(e2.salary)   # 50000 (unaffected by e1's raise)


# Key concepts learned:
# class      -> blueprint for objects
# object     -> instance created from a class
# __init__   -> special method that runs when object is created
# self       -> refers to the specific object
# method     -> a function that belongs to a class
# Each object has its own independent data (e1 and e2 don't affect each other)
