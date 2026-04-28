class GwaAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.top_student = None
        self.highest_gwa = 0.0

    def find_top_student(self):
        """Logic to read file and find the highest GWA."""
        with open(self.filename, 'r') as file:
            for line in file:
                student_name, student_gwa = line.strip().split(',')
                student_gwa = float(student_gwa)
                if self.top_student is None or gwa < self.highest_gwa:
                    self.highest_gwa = student_gwa
                    self.top_student = student_name

    def display_result(self):
        """Logic to print the top student's info."""
        pass