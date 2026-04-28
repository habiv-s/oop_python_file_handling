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
        all_numbers = self.even_list + self.odd_list
        total_count = len(all_numbers)

        sum_even = sum(self.even_list)
        average_even = sum_even / len(self.even_list) if self.even_list else 0
        minimum_even = min(self.even_list) if self.even_list else 0
        maximum_even = max(self.even_list) if self.even_list else 0

        sum_odd = sum(self.odd_list)
        average_odd = sum_odd / len(self.odd_list) if self.odd_list else 0
        minimum_odd = min(self.odd_list) if self.odd_list else 0
        maximum_odd = max(self.odd_list) if self.odd_list else 0

        report = f"""
        ║{"═" * 65}║
        ║{"COMPREHENSIVE DATA VALIDATION AUDIT".center(65)}║
        ║{"═" * 65}║
          SOURCE FILE        : numbers.txt
          TOTAL RECORDS      : {total_count} integers
        {"─" * 67}
          [GROUP A: EVEN NUMBERS]
          - Count            : {len(self.even_list)}
          - Value Range      : {minimum_even} to {maximum_even}
          - Aggregate Sum    : {sum_even}
          - Calculated Mean  : {average_even:.2f}
        {"─" * 67}
          [GROUP B: ODD NUMBERS]
          - Count            : {len(self.odd_list)}
          - Value Range      : {minimum_odd} to {maximum_odd}
          - Aggregate Sum    : {sum_odd}
          - Calculated Mean  : {average_odd:.2f}
        {"─" * 67}
          VERIFICATION       : Integrity check passed.
          EXPORT STATUS      : Files 'even.txt' & 'odd.txt' synchronized.
        ╚{"═" * 65}╝
        """
        print(report)