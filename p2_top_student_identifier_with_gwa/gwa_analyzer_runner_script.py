from gwa_analyzer import GwaAnalyzer

analyzer = GwaAnalyzer("students_and_gwa.txt")
analyzer.find_top_student()
analyzer.display_result()
analyzer.issue_digital_certificates()
analyzer.generate_honors_report()