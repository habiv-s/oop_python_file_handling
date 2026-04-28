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

        if not self.top_student:
            return

        for student in self.top_student:
            certificate = f"""
            ╔{"═" * 60}╗
            ║{"CERTIFICATE OF ACADEMIC EXCELLENCE".center(60)}║
            ╠{"═" * 60}╣
            ║{" ".center(60)}║
            ║{"This is to certify that".center(60)}║
            ║{student.upper().center(60)}║
            ║{" ".center(60)}║
            ║{"has achieved the HIGHEST GENERAL WEIGHTED AVERAGE".center(60)}║
            ║{f"with a remarkable grade of {self.highest_gwa}".center(60)}║
            ║{" ".center(60)}║
            ║{"─" * 40:^60}║
            ║{now.center(60)}║
            ║{"Date Issued".center(60)}║
            ╚{"═" * 60}╝
                    """
            print(certificate)
        print(f"Congratulations to our top {len(self.top_student)} performer(s)!")

    def generate_honors_report(self):
        """Categorizes students into academic honor levels."""
        self.first_honors = []
        self.second_honors = []
        self.total_students = 0

        with open(self.filename, 'r') as file:
            for line in file:
                student_name, student_gwa = line.strip().split(',')
                student_gwa = float(student_gwa)
                self.total_students += 1
                if 1.00 <= student_gwa <= 1.25:
                    self.first_honors.append(student_name)
                elif 1.26 <= student_gwa <= 1.50:
                    self.second_honors.append(student_name)

        centered_first = "\n".join(
            [name.center(56) for name in self.first_honors]) if self.first_honors else "None".center(56)
        centered_second = "\n".join(
            [name.center(56) for name in self.second_honors]) if self.second_honors else "None".center(56)
        centered_tops = "\n".join([name.center(56) for name in self.top_student])

        report = f"""
        ╔{"═" * 54}╗
          ACADEMIC YEAR      : 2025-2026
          RECORDS EVALUATED  : {self.total_students} Students
        {"─" * 56}
          [CATEGORY 1: FIRST HONORS (1.00 - 1.25)]
          - Qualified count  : {len(self.first_honors)}
          - Members          :
          {centered_first}
        {"─" * 56}
          [CATEGORY 2: SECOND HONORS (1.26 - 1.50)]
          - Qualified count  : {len(self.second_honors)}
          - Members          : 
          {centered_second}
        {"─" * 56}
          TOP PERFORMER(S)   : 
          {centered_tops}
          ESTABLISHED GWA    : {self.highest_gwa}
        ╚{"═" * 54}╝
        """
        print(report)