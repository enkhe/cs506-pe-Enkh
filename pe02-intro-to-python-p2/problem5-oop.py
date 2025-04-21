"""
Problem 05 - OOP

Make User class and Animal class.

CS506 - Programming for Computing
Author: Enkh Baterdene
Date: April 20, 2025
"""

class User:
    """
    Represents a user profile with basic attributes and methods
    to describe and greet the user.
    """
    def __init__(self, first_name, last_name, email, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"User Profile:\n"
              f"  Name : {self.first_name} {self.last_name}\n"
              f"  Email: {self.email}\n"
              f"  Age  : {self.age}\n"
              f"  City : {self.city}\n")

    def greet_user(self):
        print(f"Hello {self.first_name}! Welcome back to the portal.\n")


def main_part1():
    print("=== User Profiles ===\n")

    user1 = User("Alice", "Johnson", "alice@example.com", 28, "Seattle")
    user2 = User("Bob", "Smith", "bob@example.com", 35, "New York")

    user1.describe_user()
    user1.greet_user()

    user2.describe_user()
    user2.greet_user()



# Showcasing multilevel inheritance with Animal, Dog, and Puppy classes
class Animal:
    def speak(self):
        print("Animal makes their own kinds of sounds.")

class Dog(Animal):
    def bark(self):
        print("Dog barks. Woof! Woof!")

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps. Whimper! Whimper!")

def main_part2():
    print("\n=== Multilevel Inheritance ===\n")

    my_puppy = Puppy()
    my_puppy.speak()  # From Animal
    my_puppy.bark()   # From Dog
    my_puppy.weep()   # Own method


if __name__ == "__main__":
    main_part1()
    main_part2()
