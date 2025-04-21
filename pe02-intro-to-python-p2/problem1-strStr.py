"""
Problem 01 - Find substring occurrence

Finds the first occurrence of a substring in a string.

CS506 - Programming for Computing
Author: Enkh Baterdene
Date: April 20, 2025
"""

class StringOccurrence:
    """
    Finds the first occurrence of a substring in a string.
    """
    def __init__(self, haystack: str, needle: str):
        self.haystack = haystack 
        self.needle = needle

    def strStr(self) -> int:
        if self.needle == "":
            return 0
        lenHaystack = len(self.haystack)
        lenNeedle = len(self.needle)
        rangeLimit = lenHaystack - lenNeedle + 1  
        for i in range(rangeLimit):
            haystackSubString = self.haystack[i : i + lenNeedle]
            if haystackSubString == self.needle:
                return i
        return -1


def main():
    print("Program has started.\n")

    test_program("hello", "ll")
    test_program("aaaaa", "bba")
    test_program("abc", "")

    print("\nProgram has ended.")


def test_program(haystack: str, needle: str):
    occurrence = StringOccurrence(haystack, needle)
    result = occurrence.strStr()
    print(f"The first occurrence of the substring is at index: {result}")


if __name__ == "__main__":
    main()
