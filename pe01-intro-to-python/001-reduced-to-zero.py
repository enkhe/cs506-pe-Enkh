class Solution:
    def numberOfSteps(self, num: int) -> int:
        # Initialize a counter to track the number of operations
        steps = 0

        # Continue until the number becomes 0
        while num > 0:
            if num % 2 == 0:
                # If the number is even, divide it by 2
                num //= 2
            else:
                # If the number is odd, subtract 1
                num -= 1
            # Increment step counter after each operation
            steps += 1

        # Return the total number of steps
        return steps

def main():
    # Create an instance of the Solution class
    solver = Solution()

    # List of test cases to evaluate
    test_cases = [14, 8, 123, 0, 1]

    # Loop through each test case
    for num in test_cases:
        # Print the result of numberOfSteps for the current number
        print(f"Steps to reduce {num} to zero: {solver.numberOfSteps(num)}")

# Call the main function if this script is executed
if __name__ == "__main__":
    main()
