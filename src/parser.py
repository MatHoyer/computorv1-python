import re
from typing import Callable

from classes.Term import Term
from classes.Equation import Equation

number_pattern = r"[0-9]+(?:[.,][0-9]+)?"
term_pattern = fr"(?:{number_pattern}\s*\*\s*X(?:\^\d+)?|{number_pattern}\s*X(?:\^\d+)?|X(?:\^\d+)?)(?!\s*\*?\s*X)"
signed_term_pattern = fr"\s*[+\-]?\s*{term_pattern}"
side_pattern = fr"{signed_term_pattern}(?:{signed_term_pattern})*"
equation_regex = fr"^\s*({side_pattern})\s*=\s*({side_pattern})\s*$"


def parse_equation(equation: str):
    equation = equation.replace(" ", "")
    match = re.match(equation_regex, equation)
    if not match:
        for i in range(len(equation)):
            if not re.match(equation_regex, equation[:i+1]):
                print(f"Failed at char {i}: '{equation[i]}' (context: '{equation[:i+1]}')")
                break
        raise ValueError("Invalid equation: regex did not match. See above for where it failed.")

    left_member = match.group(1)
    right_member = match.group(2)

    print(left_member, right_member)
    return make_equation(left_member, right_member)


def make_equation(left_member: str, right_member: str):
    eq = Equation()
    make_terms(member=left_member, append_to_equation=eq.add_to_left_member)
    make_terms(member=right_member, append_to_equation=eq.add_to_right_member)

    return eq


def make_terms(member: str, append_to_equation: Callable[[Term], None]):
    for raw_term in re.split(r'[+-]', member):
        append_to_equation(make_term(raw_term))


def make_term(term: str):
    if "X" not in term:
        return Term(value=float(term), degree=0)

    term = term.replace("^", "")
    term = term.replace("*", "")
    splitted_term = term.split("X")
    print(term, splitted_term)
    if splitted_term[0] == "":
        splitted_term[0] = "1"
    if splitted_term[1] == "":
        splitted_term[1] = "1"

    return Term(value=float(splitted_term[0]), degree=float(splitted_term[1]))
