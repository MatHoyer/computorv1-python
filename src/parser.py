class Parser:
    def __init__(self, equation: str):
        self.equation = equation
        self.tokens = self._parse_equation()

    def _parse_equation(self):
        print(self.equation)
        return []
