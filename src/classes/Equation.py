from typing import Literal
from .Term import Term


class EquationMember:
    def __init__(self):
        self.terms: dict[float, list[Term]] = {}

    def add(self, term: Term):
        if term.degree not in self.terms:
            self.terms[term.degree] = []
        self.terms[term.degree].append(term)

    def clear(self):
        self.terms = {}

    def _get_sorted_terms(self):
        """
          #### first_term = terms_sorted_degree[0][1][0]
          0 for the highest degree\n
          1 for accessing the Term's list of the highest degree\n
          0 for accessing the first Term of this list\n
        """
        return sorted(self.terms.items(), key=lambda x: x[0])[::-1]

    def __str__(self):
        if len(self.terms) == 0:
            return "0"

        terms_sorted_degree = self._get_sorted_terms()

        is_first_term = True
        returned_string = ""
        for term_degree in terms_sorted_degree:
            for term in term_degree[1]:
                if is_first_term:
                    is_first_term = False
                    returned_string += f"{term}"
                    continue

                returned_string += " "
                returned_string += f"{term.get_str_signed()}"

        return returned_string

    def simplify(self):
        terms_sorted_degree = self._get_sorted_terms()
        new_terms = {}

        for term_degree in terms_sorted_degree:
            sum_of_terms = Term(value=0, degree=term_degree[0])
            for term in term_degree[1]:
                sum_of_terms += term
            new_terms[term_degree[0]] = [sum_of_terms]

        self.terms = new_terms


class Equation:
    def __init__(self):
        self.right_member = EquationMember()
        self.left_member = EquationMember()

    def add_to_member(self, side: Literal["left", "right"], term: Term):
        if side == "left":
            self.left_member.add(term)
        elif side == "right":
            self.right_member.add(term)
        else:
            raise ValueError(f"Invalid side: {side}")

    def __str__(self):
        return f"{self.left_member} = {self.right_member}"
