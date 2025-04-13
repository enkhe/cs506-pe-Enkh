class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # If the list is empty, return 0 as there are no unique elements
        if not nums:
            return 0

        # This index indicates where the next unique element will be placed
        write_index = 1

        # Start iterating from the second element
        for i in range(1, len(nums)):
            # If current element is different from the previous one
            if nums[i] != nums[i - 1]:
                # Write the current unique element at write_index
                nums[write_index] = nums[i]
                # Move the write_index to the next position
                write_index += 1

        # Return the number of unique elements
        return write_index

def main():
    # Create an instance of the Solution class
    solver = Solution()

    # Define test cases with sorted arrays (may have duplicates)
    test_cases = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        [],
        [1, 2, 3],
        [1, 1, 1, 1, 1]
    ]

    # Loop through each test case
    for nums in test_cases:
        # Make a copy of the original input for display
        original = nums.copy()

        # Call the removeDuplicates method and get the count of unique items
        length = solver.removeDuplicates(nums)

        # Print before and after arrays
        print(f"Original: {original} → Unique: {nums[:length]} (Length: {length})")

# Call the main function if this script is executed
if __name__ == "__main__":
    main()
