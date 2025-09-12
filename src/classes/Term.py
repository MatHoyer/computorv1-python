def format_float(value: float):
    if value.is_integer():
        return int(value)
    return value


class Term:
    def __init__(self, value: float, degree: float = 1):
        self.degree = degree
        self.value = abs(value)
        self.sign = 1 if value >= 0 else -1

    def __str__(self):
        if self.degree == 0 or self.value == 0:
            return f"{format_float(self.value * self.sign)}"

        printed_degree = f"^{format_float(self.degree)}" if self.degree != 1 else ""

        printed_value = ""
        if self.value * self.sign != 1 and self.value * self.sign != -1:
            printed_value = f"{format_float(self.value * self.sign)}"
        elif self.value * self.sign == -1:
            printed_value = "-"

        return f"{printed_value}X{printed_degree}"

    def __repr__(self):
        return self.__str__()

    def get_str_signed(self):
        return f"{"+ " if self.sign == 1 else "- "}{self.absolute()}"

    def opposite(self):
        return Term(-(self.value * self.sign), self.degree)

    def absolute(self):
        return Term(abs(self.value), self.degree)

    def __add__(self, other: "Term"):
        if self.degree != other.degree:
            raise NotImplementedError("Terms must have the same degree to add")

        new_value = self.value * self.sign + other.value * other.sign

        return Term(new_value, self.degree)

    def __sub__(self, other: "Term"):
        if self.degree != other.degree:
            raise NotImplementedError("Terms must have the same degree to subtract")

        new_value = self.value * self.sign - other.value * other.sign

        return Term(new_value, self.degree)

    def __mul__(self, other: "Term"):
        new_value = (self.value * self.sign) * (other.value * other.sign)
        return Term(new_value, self.degree + other.degree)

    def __truediv__(self, other: "Term"):
        new_value = (self.value * self.sign) / (other.value * other.sign)
        return Term(new_value, self.degree - other.degree)

    def __eq__(self, other: "Term"):
        return self.degree == other.degree and self.value == other.value and self.sign == other.sign
