from src.classes.Equation import EquationMember, Equation
from src.classes.Term import Term


def test_equation_member_str():
    equation_member = EquationMember()
    assert str(equation_member) == "0"

    equation_member.add(Term(value=1, degree=0))
    equation_member.add(Term(value=1, degree=2))
    equation_member.add(Term(value=1, degree=1))
    assert str(equation_member) == "X^2 + X + 1"

    equation_member.clear()
    assert str(equation_member) == "0"

    equation_member.add(Term(value=-2, degree=1))
    equation_member.add(Term(value=-1, degree=0))
    equation_member.add(Term(value=-1, degree=2))
    assert str(equation_member) == "-X^2 - 2X - 1"


def test_equation_member_simplify():
    equation_member = EquationMember()
    equation_member.add(Term(value=1, degree=0))
    equation_member.add(Term(value=1, degree=2))
    equation_member.add(Term(value=1, degree=2))
    equation_member.add(Term(value=1, degree=2))
    equation_member.add(Term(value=1, degree=1))
    assert str(equation_member) == "X^2 + X^2 + X^2 + X + 1"

    equation_member.simplify()
    assert str(equation_member) == "3X^2 + X + 1"


def test_equation_str():
    equation = Equation()
    equation.add_to_member("left", Term(value=1, degree=0))
    equation.add_to_member("left", Term(value=1, degree=2))
    equation.add_to_member("left", Term(value=1, degree=1))
    assert str(equation) == "X^2 + X + 1 = 0"

    equation.add_to_member("right", Term(value=1, degree=1))
    equation.add_to_member("right", Term(value=1, degree=2))
    equation.add_to_member("right", Term(value=1, degree=0))
    equation.add_to_member("right", Term(value=1, degree=1))
    assert str(equation) == "X^2 + X + 1 = X^2 + X + X + 1"
