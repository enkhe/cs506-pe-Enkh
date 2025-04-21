"""
Problem 06 - Working with Files

Working with Files

CS506 - Programming for Computing
Author: Enkh Baterdene
Date: April 20, 2025
"""


class WordCounter:
    """
    Counts the number of words in a given text file.
    """
    def __init__(self, filename: str):
        self.filename = filename

    def count_words(self) -> int:
        try:
            with open(self.filename, 'r') as file:
                text = file.read()
                words = text.split()
                return len(words)
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
            return 0


class GuestBook:
    """
    Logs visitor names into guest_book.txt with greetings.
    """
    def __init__(self, filename="guest_book.txt"):
        self.filename = filename

    def prompt_visitors(self):
        print("Enter 'q' to quit.")
        while True:
            name = input("Enter your name: ")
            if name.lower() == 'q':
                break
            print(f"Hello, {name}! Nice to see you!")
            with open(self.filename, 'a') as file:
                file.write(f"{name} visited.\n")



class AnimalFileReader:
    """
    Reads contents of cats.txt and dogs.txt, handles missing files.
    """
    def __init__(self, filenames):
        self.filenames = filenames

    def display_animals(self):
        for filename in self.filenames:
            try:
                with open(filename, 'r') as file:
                    print(f"\nContents of {filename}:")
                    print(file.read())
            except FileNotFoundError:
                print(f"The file '{filename}' is missing. Please check the file name!")


def main():
    print("=== File Word Counter ===")
    wc = WordCounter("sample.txt")
    word_count = wc.count_words()
    print(f"Word count: {word_count}")

    print("\n=== Guest Book ===")
    guest_book = GuestBook()
    guest_book.prompt_visitors()

    print("\n=== Reading Animal Files ===")
    reader = AnimalFileReader(["cats.txt", "dogs.txt"])
    reader.display_animals()


if __name__ == "__main__":
    main()














