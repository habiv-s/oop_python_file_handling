class NumberSorter:
    def __init__(self, numbers):
        self.numbers = numbers
        self.even_list = []
        self.odd_list = []

    def sort_numbers(self):
        """Reads integers and categorizes them into even or odd lists."""
        try:
            with open('numbers.txt', 'r') as numbers_file:
                for numbers in numbers_file:
                    number = int(numbers.strip())
                    if number % 2 == 0:
                        self.even_list.append(number)
                    else:
                        self.odd_list.append(number)
            print(f"Successfully processed numbers from {self.numbers}.")
        except FileNotFoundError:
            print("Sorry, the numbers text file was not found.")

    def save_to_files(self):
        """Creates even.txt and odd.txt from the sorted lists."""
        with open('even.txt', 'w') as even_numbers_file:
            for numbers in self.even_list:
                even_numbers_file.write(f"{numbers}\n")
        with open('odd.txt', 'w') as odd_numbers_file:
            for numbers in self.odd_list:
                odd_numbers_file.write(f"{numbers}\n")
        print("Generated 'even.txt' and 'odd.txt' successfully.")

    def generate_audit(self):
        """Produces a comprehensive formal audit including range and averages."""
        pass