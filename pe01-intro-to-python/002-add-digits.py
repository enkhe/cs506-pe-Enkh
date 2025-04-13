class Solution:
    def addDigitsLoop(self, num: int) -> int:
        # Loop until the number becomes a single digit
        while num >= 10:
            # Convert the number to a string, then sum its digits
            num = sum(int(d) for d in str(num))
        # Return the resulting single digit
        return num

    def addDigitsNoLoop(self, num: int) -> int:
        # Use the digital root formula to find the result in constant time
        return 0 if num == 0 else 1 + (num - 1) % 9

def main():
    # Create an instance of the Solution class
    solver = Solution()

    # List of test cases to evaluate
    test_cases = [38, 0, 9, 99, 123456]

    # Loop through each test case
    for num in test_cases:
        # Get results from both methods
        loop_result = solver.addDigitsLoop(num)
        const_result = solver.addDigitsNoLoop(num)

        # Print both results for comparison
        print(f"addDigitsLoop({num}) = {loop_result}, addDigitsNoLoop({num}) = {const_result}")

# Call the main function if this script is executed
if __name__ == "__main__":
    main()
