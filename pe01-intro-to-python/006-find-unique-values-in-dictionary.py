class Solution:
    def findUniqueValues(self, dict_list: list[dict]) -> set:
        # Initialize an empty set to store unique values
        unique_values = set()

        # Loop through each dictionary in the list
        for d in dict_list:
            # Loop through each value in the current dictionary
            for value in d.values():
                # Add the value to the set (duplicates are ignored)
                unique_values.add(value)

        # Return the set of unique values
        return unique_values

def main():
    # Sample input data: list of dictionaries
    sample_data = [
        {"V": "S001"},
        {"V": "S002"},
        {"VI": "S001"},
        {"VI": "S005"},
        {"VII": "S005"},
        {"V": "S009"},
        {"VIII": "S007"}
    ]

    # Create an instance of the Solution class
    solver = Solution()

    # Call the function to get the unique values
    result = solver.findUniqueValues(sample_data)

    # Print the result
    print(f"Unique Values: {result}")

# Execute main() if this script is run directly
if __name__ == "__main__":
    main()
