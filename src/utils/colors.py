class Colors:
    FAIL = "\033[91m"
    OKBLUE = "\033[94m"
    WARNING = "\033[93m"
    OKGREEN = "\033[92m"
    OKCYAN = "\033[96m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    HEADER = "\033[95m"
    UNDERLINE = "\033[4m"

    def __init__(self, value) -> None:
        self.value = str(value)

    def fail(self):
        return f"{self.FAIL}{self.value}{self.ENDC}"

    def okBlue(self):
        return f"{self.OKBLUE}{self.value}{self.ENDC}"

    def warning(self):
        return f"{self.WARNING}{self.value}{self.ENDC}"

    def okGreen(self):
        return f"{self.OKGREEN}{self.value}{self.ENDC}"

    def okCyan(self):
        return f"{self.OKCYAN}{self.value}{self.ENDC}"

    def okBold(self):
        return f"{self.BOLD}{self.value}{self.ENDC}"

    def underline(self):
        return f"{self.UNDERLINE}{self.value}{self.ENDC}"
    
    def underline_fail(self):
        return f"{self.UNDERLINE}{self.FAIL}{self.value}{self.ENDC}"
    
