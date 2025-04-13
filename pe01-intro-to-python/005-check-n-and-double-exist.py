class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        # Create a set to store the elements we've seen so far
        seen = set()

        # Iterate over each number in the input array
        for num in arr:
            # Check if the double of the current number has been seen
            if 2 * num in seen:
                return True  # Found M earlier such that M = N / 2

            # Check if the half (only if even) of the current number has been seen
            if num % 2 == 0 and num // 2 in seen:
                return True  # Found M earlier such that N = 2 * M

            # Add the current number to the set
            seen.add(num)

        # If no such pair is found, return False
        return False

def main():
    # Create an instance of the Solution class
    solver = Solution()

    # Define multiple test cases
    test_cases = [
        [10, 2, 5, 3],     # True: 10 = 2 * 5
        [7, 1, 14, 11],    # True: 14 = 2 * 7
        [3, 1, 7, 11],     # False: no N = 2 * M pair
        [0, 0],            # True: 0 = 2 * 0, and indices i != j
        [-2, 0, 10, -5],   # False
        [-10, -5, 20, 40], # True: 20 = 2 * 10 or 40 = 2 * 20
    ]

    # Run each test case and print the result
    for arr in test_cases:
        result = solver.checkIfExist(arr)
        print(f"Input: {arr} → Output: {result}")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
