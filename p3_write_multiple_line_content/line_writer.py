from datetime import datetime

from practice_python_programs.lstrip_same_functionality import user_input


class LifeRecorder:
    def __init__(self, filename="mylife.txt"):
        self.filename = filename
        self.purple = "\033[95m"
        self.cyan = "\033[96m"
        self.yellow = "\033[93m"
        self.reset = "\033[0m"

    def record_lines(self):
        """Writes interactive user input into a file with timestamps."""
        print(f"{self.purple}--- Welcome to your Personal Diary ---{self.reset}")
        with open(self.filename, 'a') as file:
            while True:
                user_input = input(f"{self.yellow}Enter line: {self.reset}")

                choice = input(f"{self.cyan}Are there more lines y/n? {self.reset}").lower().strip()

                if choice == 'n':
                    print(f"\n{self.purple}Entry saved.{self.reset}")
                    break