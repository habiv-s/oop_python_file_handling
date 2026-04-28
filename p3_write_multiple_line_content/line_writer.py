class LifeRecorder:
    def __init__(self, filename="mylife.txt"):
        self.filename = filename
        self.purple = "\033[95m"
        self.cyan = "\033[96m"
        self.yellow = "\033[93m"
        self.reset = "\033[0m"

    def record_lines(self):
        """Writes interactive user input into a file with timestamps."""
        pass