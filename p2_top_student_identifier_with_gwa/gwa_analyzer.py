class GwaAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.top_student = []
        self.highest_gwa = None

    def find_top_student(self):
        """Logic to read file and find the highest GWA."""
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    student_name, student_gwa = line.strip().split(',')
                    student_gwa = float(student_gwa)
                    if self.highest_gwa is None or student_gwa < self.highest_gwa:
                        self.highest_gwa = student_gwa
                        self.top_student = [student_name]
                    elif student_gwa == self.highest_gwa:
                        self.top_student.append(student_name)
            print("Successfully processed student records.")
        except FileNotFoundError:
            print("Error: File not found.")

    def display_result(self):
        """Logic to print the top student's info."""
        if self.top_student:
            print("\nTOP STUDENT IDENTIFIED")
            print(f"GWA: {self.highest_gwa}")
            print("Name(s):")
            for student in self.top_student:
                print(f" - {student}")
        else:
            print("No student data available to display.")

    def issue_digital_certificates(self):
        """Generates a formal digital certificate for the top performer(s)."""
        from datetime import datetime
        now = datetime.now().strftime("%B %d, %Y")

    def generate_honors_report(self):
        """Categorizes students into academic honor levels."""
        pass