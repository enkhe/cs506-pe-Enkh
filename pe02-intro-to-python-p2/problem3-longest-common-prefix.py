"""
Problem 03 - Longest Common Prefix

Finds the longest common prefix among a list of strings.

CS506 - Programming for Computing
Author: Enkh Baterdene
Date: April 20, 2025
"""

class CommonPrefixFinder:
    """
    Finds the longest common prefix among a list of strings.
    """
    def __init__(self, words: list[str]):
        self.words = words

    def longestCommonPrefix(self) -> str:
        if not self.words:
            return ""

        # Start with the first word as the prefix to check against others
        prefix = self.words[0]

        for word in self.words[1:]:
            # Shorten the prefix until it's a prefix of the current word
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix


def main():
    print("Common Prefix Finder Program\n")

    test_prefix(["flower", "flow", "flight"])
    test_prefix(["dog", "racecar", "car"])
    test_prefix(["interview", "interval", "internal", "internet"])
    test_prefix([""])  # Edge case: empty string
    test_prefix([])    # Edge case: empty list

    print("\nProgram Complete.")


def test_prefix(words: list[str]):
    finder = CommonPrefixFinder(words)
    result = finder.longestCommonPrefix()
    print(f"Longest common prefix in {words} is: \"{result}\"")


if __name__ == "__main__":
    main()
