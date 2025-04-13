class Solution:
    def reverseString(self, s: list[str]) -> None:
        # Initialize two pointers: one from the start, one from the end
        left, right = 0, len(s) - 1

        # Continue swapping until the two pointers meet
        while left < right:
            # Swap the characters at the left and right pointers
            s[left], s[right] = s[right], s[left]
            # Move the left pointer one step to the right
            left += 1
            # Move the right pointer one step to the left
            right -= 1

        # This function modifies the input list in place and returns nothing

def main():
    # Create an instance of the Solution class
    solver = Solution()

    # Define several test cases with different input strings
    test_cases = [
        ["h", "e", "l", "l", "o"],
        ["H", "a", "n", "n", "a", "h"],
        ["1", "2", "3", "4", "5"],
        ["a"],
        []
    ]

    # Loop through each test case
    for chars in test_cases:
        # Make a copy of the original input for display
        original = chars.copy()

        # Call the reverseString method to reverse the list
        solver.reverseString(chars)

        # Print before and after lists
        print(f"Original: {original} → Reversed: {chars}")

# Call the main function if this script is executed
if __name__ == "__main__":
    main()
