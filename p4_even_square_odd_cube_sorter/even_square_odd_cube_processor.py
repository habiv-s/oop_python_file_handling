from datetime import datetime

class PowerProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.squares = []
        self.cubes = []

    def process_numbers(self):
        """Reads integers from the source file and applies square/cube logic."""
        try:
            with open(self.filename, 'r') as file:
                for integers in file:
                    integer = int(integers.strip())
                    if integer % 2 == 0:
                        self.squares.append(integer ** 2)
                    else:
                        self.cubes.append(integer ** 3)
            print("Even and Odd numbers identified. Squares and Cubes calculation complete!")
        except FileNotFoundError:
            print("Sorry, the integers text file was not found.")

    def save_results(self):
        """Writes the transformed results into double.txt and triple.txt."""
        with open("double.txt", 'w') as double_file:
            for square in self.squares:
                double_file.write(f"{square}\n")
        with open("triple.txt", 'w') as triple_file:
            for cube in self.cubes:
                triple_file.write(f"{cube}\n")
        print("Results saved to double.txt and triple.txt.")

    def calculate_statistics(self):
        """Calculates counts and averages."""
        squares_count = len(self.squares)
        cubes_count = len(self.cubes)
        if squares_count > 0:
            squares_average = sum(self.squares) / squares_count
        else:
            squares_average = 0
        if cubes_count > 0:
            cubes_average = sum(self.cubes) / cubes_count
        else:
            cubes_average = 0
        return squares_count, cubes_count, squares_average, cubes_average

    def get_report_template(self, squares_count, cubes_count, squares_average, cubes_average):
        """Defines the visual style of the report."""
        now = datetime.now().strftime("%A, %B %d, %Y")
        report = (
            f"{'=' * 34}\n"
            f"MATH TRANSFORMATION REPORT\n"
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
            f"{'-' * 34}\n"
            f"Even Numbers Squared: {squares_count}\n"
            f"Squares Average: {squares_average:.2f}\n\n"
            f"Odd Numbers Cubed: {cubes_count}\n"
            f"Cubes Average: {cubes_average:.2f}\n"
            f"{'=' * 34}\n"
        )
        return report

    def generate_report(self):
        """Saves the formatted report to a file."""
        squares_count, cubes_count, squares_average, cubes_average = self.calculate_statistics()
        final_output = self.get_report_template(squares_count, cubes_count, squares_average, cubes_average)
        with open("report.txt", 'w') as report_file:
            report_file.write(final_output)