"""
Problem 04 - Adding Numbers

Prompts the user for two numbers, adds them, and prints the result.

CS506 - Programming for Computing
Author: Enkh Baterdene
Date: April 20, 2025
"""

class NumberAdder:
    """
    Prompts the user for two numbers, adds them, and prints the result.
    Handles invalid input using exception handling.
    """

    def __init__(self):
        self.num1 = None
        self.num2 = None

    def prompt_and_add(self):
        try:
            self.num1 = int(input("Enter the first number: "))
            self.num2 = int(input("Enter the second number: "))
            total = self.num1 + self.num2
            print(f"The sum of {self.num1} and {self.num2} is: {total}")
        except ValueError:
            print("❌ Invalid input! Please enter valid numbers only.")


def main():
    print("Welcome to the Number Adder!\n")

    adder = NumberAdder()
    adder.prompt_and_add()

    print("\nProgram Complete.")


if __name__ == "__main__":
    main()
