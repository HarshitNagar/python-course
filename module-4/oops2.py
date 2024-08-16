#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        area = self.length * self.width
        return area

    def perimeter(self):
        peri = 2 * (self.width + self.length)
        return peri

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)


sample_square = Square(4)
# Square(4).area()
sample_square.perimeter()




sample_square = Square(4)
sample_square.area()
# print(sample_square)


# class Rectangle:
#   def __init__(self, length, width):
#     self.length = length
#     self.width = width
#
#   def area(self):
#     return self.length * self.width
#
#
# class Square(Rectangle):
#   def __init__(self, length):
#     super().__init__(length, length)
#
#   # def area(self):
#   #   return self.length * self.length
#
# class Cube(Square):
#   def surface_area(self):
#     face_area = super().area()
#     return face_area*6



# How are we going to depict the relationship that square is a special case of rectangle ?


# In[ ]:


rect = Rectangle(2, 3)
rect.area()

sq = Square(5)
sq.area()


# In[ ]:


# illustrate different aspects of classes in Python:

### 1. **Encapsulation**
# Encapsulation is a principle of object-oriented programming that restricts access to certain parts of an object. This is typically done by making attributes or methods private, which is signified by a leading underscore (`_`) or double underscore (`__`).

# **Example:**

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance # Private attribute
        self._status = 'live' # Protected attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance  # Accessing the private attribute via a public method


# Create an instance of BankAccount
account = BankAccount("Alice", 100)

account.deposit(50)
account.withdraw(30)

# print(account.get_balance())

# Trying to access the private attribute directly will raise an AttributeError
# print(account.__balance)  # This will raise an error


class Status(BankAccount):
    def __init__(self):
        super().__init__(self, "Anny")
        print(self._status)
        print(self.__balance)

obj = Status()
#
class Hello(Status):
    def __init__(self):
        print(self._status)
#
obj2 = Hello()



# In[ ]:


### 2. **Polymorphism**
# Polymorphism allows objects of different classes to be treated as objects of a common superclass. This is particularly useful when dealing with a group of objects that share a common interface.

# **Example:**

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    print(animal.speak())

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Output: Woof!
make_animal_speak(cat)  # Output: Meow!


# In[ ]:


### 7. **Composition**
# Composition is a design principle where one class is composed of one or more objects of other classes, creating a has-a relationship rather than an is-a relationship.

# **Example:**

class Engine:
    def start(self):
        return "Engine started."

class Wheels:
    def roll(self):
        return "Wheels rolling."

class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = Wheels()

    def drive(self):
        print(self.engine.start())
        print(self.wheels.roll())



# Create an instance of Car
my_car = Car()

my_car.drive()
# Output:
# Engine started.
# Wheels rolling.

