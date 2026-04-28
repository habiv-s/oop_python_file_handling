class PowerProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.squares = []
        self.cubes = []

    def process_numbers(self):
        """Reads integers from the source file and applies square/cube logic."""
        with open(self.filename, 'r') as file:
            for integers in file:
                integer = int(integers.strip())
                if integer % 2 == 0:
                    self.squares.append(integer ** 2)
                else:
                    self.cubes.append(integer ** 3)

    def save_results(self):
        """Writes the transformed results into double.txt and triple.txt."""
        pass