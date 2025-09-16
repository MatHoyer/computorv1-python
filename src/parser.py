import re
from typing import Callable

try:
    from .classes.Term import Term
    from .classes.Equation import Equation
except ImportError:
    from classes.Term import Term
    from classes.Equation import Equation

term_pattern = r"([+-]?)(\d*\.?\d*)(X)?(?:\^(\d+))?"

member_pattern = fr"(?:{term_pattern})*"

equation_pattern = fr"^{member_pattern}={member_pattern}$"


signs = "+-*"


def parse_equation(equation: str):
    equation = equation.replace(" ", "")
    for i in range(len(equation) - 1):
        if equation[i] in signs and equation[i + 1] in signs:
            raise ValueError(f"Invalid equation: consecutive signs '{equation[i]}{equation[i + 1]}' at position {i}")
    equation = equation.replace("*", "")

    match = re.match(equation_pattern, equation)
    if not match:
        for i in range(len(equation)):
            if not re.match(equation_pattern, equation[:i+1]):
                print(f"Failed at char {i}: '{equation[i]}' (context: '{equation[:i+1]}')")
                break
        raise ValueError("Invalid equation: regex did not match")

    members = equation.split("=")
    if len(members) != 2:
        raise ValueError("Invalid equation")

    left_member = members[0]
    right_member = members[1]

    return make_equation(left_member, right_member)


def make_equation(left_member: str, right_member: str):
    eq = Equation()
    make_terms(member=left_member, append_to_equation=eq.left_member.add)
    make_terms(member=right_member, append_to_equation=eq.right_member.add)

    return eq


SIGN_INDEX = 0
VALUE_INDEX = 1
X_INDEX = 2
DEGREE_INDEX = 3


def make_terms(member: str, append_to_equation: Callable[[Term], None]):
    terms = re.findall(term_pattern, member)

    for term in terms:
        sign = term[SIGN_INDEX]
        value = term[VALUE_INDEX]
        is_x = term[X_INDEX] == "X"
        degree = term[DEGREE_INDEX]

        if sign == "" and value == "" and is_x is False and degree == "":
            continue

        if value == "":
            value = 1
        value = float(value)

        if degree == "" and is_x:
            degree = 1
        elif degree == "":
            degree = 0
        degree = float(degree)

        if sign == "-":
            value = -value

        append_to_equation(Term(value=value, degree=degree))
