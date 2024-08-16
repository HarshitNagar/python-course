#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# What is OOP ?
# - OOP: Object Oriented Programming
# - It is a programming paradigm in which the code is structured by packing related properties and behaviours into objects.
# - For eg: Lets say you want to track employees in an organisation.
# - Properties: Name, age, gender, ID, address, contact etc.
# - Behaviours: What would you want to do with an employee ?
# - Assign department
# - get details of the employee
# - calculate employee salary
# - Using lists ?
# - ```
aman = ['aman', 30, 'M', 123]
neha = ['neha', 34, 'F', 134]
employees = [aman, neha]
# ```
# - Using dict ?
# - ```
aman = { 'name': 'aman', 'age': 30, 'gender': 'M', 'id': '123']
neha = { 'name': 'neha', 'age': 34, 'gender': 'F', 'id': '134']
employees = [aman, neha]
# ```
# - Using OOP ?


# In[34]:


class Employee:
        def __init__(self, name=None, gender=None, age=25, ident=None):
                self.name = name
                self.gender = gender
                self.ident = ident
                self.age = age
                self.salary = 0
        #
        def __str__(self):
                return f"{self.name}, {self.gender}, {self.age}"

        def __repr__(self):
                return (
                        f"{type(self).__name__}, "
                        f"name={self.name}, "
                        f"gender={self.gender}, "
                        f"ident={self.ident}, "
                        f"age={self.age}, "
                        f"salary={self.salary}"
                )

        def set_salary(self):
                self.salary = 10000
        #
        def get_emp_details(self):
                print(self.name, self.gender, self.salary, self.age, self.ident)
#
emp1 = Employee(name = 'Aman', gender = 'M', ident = 134)
# emp2 = Employee('Neha', 'F', 34, '123')
emp1.set_salary()
# print(emp1.name, emp1.age, emp1.salary)
emp1.get_emp_details()

print(emp1)
emp1


# # __str__ and __repr__ methods
# - The methods that begin and end with double underscores are called dunder methods or magic methods
# - They are a fundamental part of python's internal class mechanism. Python calls them automatically in response to specific operations
# - eg: __init__ is the most commonly known dunder method. This method is an instance initializer. This gets called automatically when a class constructor is called.
# - __str__ provides informal string representations of for objects.
#   - This method must return a string that represents the object in a user-friendly manner.
#   - You can access an object’s informal string representation using either str() or print().
# - __repr__ provides formal string representations of for objects.
#   - it must return a string that allows you to re-create the object if possible.
#   - This string representation is mostly targeted at Python programmers

# # Inheritance
# - It is the process by which once class takes on the attributes and methods of another class.
# - The class that inherits the attributes and methods is called the child class/derived class/sub class.
# - The class whose attributes and methods are inherited is called parent class/base class/super class.
# - Child class can overwrite or extend attributes and methods of parent class.

# # single inheritance

# In[36]:


class Parent:
        def func1(self):
                print("This is parent class")

class Child(Parent):
        def func2(self):
                print("This is child class")

object = Child()
object.func1()
object.func2()


# Multiple inheritance

# In[37]:


class Mother:
        mothername = ""

        def mother(self):
                print(self.mothername)

class Father:
        fathername = ""
        def father(self):
                print(self.fathername)

# Derived class

class Son(Mother, Father):
        def parents(self):
                print("Father :", self.fathername)
                print("Mother :", self.mothername)


s1 = Son()
s1.fathername = "a"
s1.mothername = "b"
s1.parents()


# Multilevel inheritance

# In[39]:


class Grandfather:

        def __init__(self, grandfathername):
                self.grandfathername = grandfathername


# Intermediate class


class Father(Grandfather):
        def __init__(self, fathername, grandfathername):
                self.fathername = fathername

                # invoking constructor of Grandfather class
                # Grandfather.__init__(self, grandfathername)

# Derived class


class Son(Father):
        def __init__(self, sonname, fathername, grandfathername):
                self.sonname = sonname
                self.fathername = fathername
                self.grandfathername = grandfathername

                # invoking constructor of Father class
                # Father.__init__(self, fathername, grandfathername)

        def print_name(self):
                print('Grandfather name :', self.grandfathername)
                print("Father name :", self.fathername)
                print("Son name :", self.sonname)


#  Driver code
s1 = Son('Sham', 'Ram', 'Pal')
print(s1.grandfathername)
print(s1.fathername)
print(s1.sonname)
s1.print_name()


# # Hierarchical inheritance

# In[16]:


class Parent:
        def func1(self):
                print("This function is in parent class.")

# Derived class1


class Child1(Parent):
        def func2(self):
                print("This function is in child 1.")

# Derivied class2


class Child2(Parent):
        def func3(self):
                print("This function is in child 2.")


# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()


# In[42]:


class A:
        def __init__(self):
                print("Class A")
        def printout(self):
                print("printout")

class B(A):
        def __init__(self):
                print("Class B")

def main():
        myA = A()
        myB = B()
        myB.printout()

if __name__ == '__main__':
        main()


# In[46]:




