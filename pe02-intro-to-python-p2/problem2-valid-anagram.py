"""
Problem 02 - Valid Anagram

Checks if two strings are valid anagrams of each other.

CS506 - Programming for Computing
Author: Enkh Baterdene
Date: April 20, 2025
"""

class AnagramChecker:
    """
    Checks if two strings are valid anagrams of each other.
    """
    def __init__(self, s: str, t: str):
        self.s = s
        self.t = t

    def isAnagram(self) -> bool:
        if len(self.s) != len(self.t):
            return False

        # Create dictionaries to count character occurrences
        countS = {}
        countT = {}

        for char in self.s:
            countS[char] = countS.get(char, 0) + 1

        for char in self.t:
            countT[char] = countT.get(char, 0) + 1

        return countS == countT


def main():
    print("Anagram Checker Program\n")

    test_anagram("anagram", "nagaram")  # True
    test_anagram("rat", "car")          # False
    test_anagram("listen", "silent")    # True
    test_anagram("hello", "helloo")     # False

    print("\nProgram Complete.")


def test_anagram(s: str, t: str):
    checker = AnagramChecker(s, t)
    result = checker.isAnagram()
    print(f"Are \"{s}\" and \"{t}\" anagrams? Result: {result}")


if __name__ == "__main__":
    main()
