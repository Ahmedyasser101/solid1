# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 07:56:39 2024

@author: lap
"""

"""1. Single Responsibility Principle (SRP)
A class should have only one reason to change, meaning it should have only one job or responsibility."""
# Before SRP
class User:
    def _init_(self, name, email):
        self.name = name
        self.email = email
    
    def save_to_database(self):
        # Code to save user to database
        pass
    
    def send_welcome_email(self):
        # Code to send email
        pass


# After SRP: Split responsibilities into different classes
class User:
    def _init_(self, name, email):
        self.name = name
        self.email = email

class UserDatabase:
    def save(self, user):
        # Code to save user to database
        pass

class EmailService:
    def send_welcome_email(self, user):
        # Code to send email
        pass

"""2. Open/Closed Principle (OCP)
A class should be open for extension but closed for modification. 
This means you should be able to add new functionality without changing existing code."""

# Before OCP
class Discount:
    def calculate(self, product):
        if product.category == "electronics":
            return product.price * 0.1
        elif product.category == "clothing":
            return product.price * 0.2


# After OCP: Add new categories without modifying Discount class
class Discount:
    def calculate(self, product):
        raise NotImplementedError

class ElectronicsDiscount(Discount):
    def calculate(self, product):
        return product.price * 0.1

class ClothingDiscount(Discount):
    def calculate(self, product):
        return product.price * 0.2


"""3. Liskov Substitution Principle (LSP)
Objects of a superclass should be replaceable with objects of a subclass without"
 affecting the correctness of the program."""
 # Before LSP
class Bird:
    def fly(self):
        pass

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches cannot fly")

# After LSP: Avoid breaking behavior for subclasses
class Bird:
    def move(self):
        pass

class Sparrow(Bird):
    def move(self):
        print("Flying")

class Ostrich(Bird):
    def move(self):
        print("Running")


"""4. Interface Segregation Principle (ISP)
A client should not be forced to implement interfaces it doesn't use. 
In other words, create smaller, more specific interfaces rather than large, general ones."""
# Before ISP
class Worker:
    def work(self):
        pass
    
    def eat(self):
        pass

class Robot(Worker):
    def work(self):
        pass
    
    def eat(self):
        raise Exception("Robots don't eat")

# After ISP: Split responsibilities into smaller interfaces
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        pass
    
    def eat(self):
        pass

class Robot(Workable):
    def work(self):
        pass


"""5. Dependency Inversion Principle (DIP)
High-level modules should not depend on low-level modules. 
Both should depend on abstractions (e.g., interfaces). 
Abstractions should not depend on details. Details should depend on abstractions."""
# Before DIP
class LightBulb:
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass

class Switch:
    def _init_(self, bulb):
        self.bulb = bulb
    
    def operate(self):
        self.bulb.turn_on()  # Switch depends directly on LightBulb


# After DIP: Use abstraction (interface)
class Switchable:
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass

class Switch:
    def _init_(self, device: Switchable):
        self.device = device
    
    def operate(self):
        self.device.turn_on()