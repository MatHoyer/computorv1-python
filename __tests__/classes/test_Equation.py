from src.classes.Equation import EquationMember, Equation
from src.classes.Term import Term


def test_equation_member_init():
    """Test EquationMember initialization"""
    equation_member = EquationMember()
    assert equation_member.terms == {}
    assert str(equation_member) == "0"


def test_equation_member_add():
    """Test adding terms to EquationMember"""
    equation_member = EquationMember()

    # Add first term
    term1 = Term(value=1, degree=2)
    equation_member.add(term1)
    assert 2 in equation_member.terms
    assert len(equation_member.terms[2]) == 1
    assert equation_member.terms[2][0] == term1

    # Add term with same degree
    term2 = Term(value=3, degree=2)
    equation_member.add(term2)
    assert len(equation_member.terms[2]) == 2

    # Add term with different degree
    term3 = Term(value=5, degree=1)
    equation_member.add(term3)
    assert 1 in equation_member.terms
    assert len(equation_member.terms[1]) == 1


def test_equation_member_clear():
    """Test clearing EquationMember"""
    equation_member = EquationMember()
    equation_member.add(Term(value=1, degree=2))
    equation_member.add(Term(value=1, degree=1))

    equation_member.clear()
    assert equation_member.terms == {}
    assert str(equation_member) == "0"


def test_equation_member_str_empty():
    """Test string representation of empty EquationMember"""
    equation_member = EquationMember()
    assert str(equation_member) == "0"


def test_equation_member_str_single_terms():
    """Test string representation with single terms"""
    equation_member = EquationMember()

    # Constant term
    equation_member.add(Term(value=5, degree=0))
    assert str(equation_member) == "5"

    equation_member.clear()
    equation_member.add(Term(value=-3, degree=0))
    assert str(equation_member) == "-3"

    # Linear term
    equation_member.clear()
    equation_member.add(Term(value=1, degree=1))
    assert str(equation_member) == "X"

    equation_member.clear()
    equation_member.add(Term(value=-1, degree=1))
    assert str(equation_member) == "-X"

    equation_member.clear()
    equation_member.add(Term(value=2, degree=1))
    assert str(equation_member) == "2X"

    # Quadratic term
    equation_member.clear()
    equation_member.add(Term(value=1, degree=2))
    assert str(equation_member) == "X^2"

    equation_member.clear()
    equation_member.add(Term(value=3, degree=2))
    assert str(equation_member) == "3X^2"


def test_equation_member_str_multiple_terms():
    """Test string representation with multiple terms"""
    equation_member = EquationMember()

    # Standard order: highest degree first
    equation_member.add(Term(value=1, degree=0))
    equation_member.add(Term(value=1, degree=2))
    equation_member.add(Term(value=1, degree=1))
    assert str(equation_member) == "X^2 + X + 1"

    # With negative terms
    equation_member.clear()
    equation_member.add(Term(value=-2, degree=1))
    equation_member.add(Term(value=-1, degree=0))
    equation_member.add(Term(value=-1, degree=2))
    assert str(equation_member) == "-X^2 - 2X - 1"

    # Mixed signs
    equation_member.clear()
    equation_member.add(Term(value=2, degree=2))
    equation_member.add(Term(value=-3, degree=1))
    equation_member.add(Term(value=4, degree=0))
    assert str(equation_member) == "2X^2 - 3X + 4"


def test_equation_member_str_zero_coefficients():
    """Test string representation with zero coefficients"""
    equation_member = EquationMember()
    equation_member.add(Term(value=0, degree=2))
    equation_member.add(Term(value=0, degree=1))
    assert str(equation_member) == "0 + 0"


def test_equation_member_str_decimal_values():
    """Test string representation with decimal values"""
    equation_member = EquationMember()
    equation_member.add(Term(value=2.5, degree=2))
    equation_member.add(Term(value=-1.75, degree=1))
    equation_member.add(Term(value=3, degree=0))
    assert str(equation_member) == "2.5X^2 - 1.75X + 3"


def test_equation_member_simplify():
    """Test simplifying EquationMember"""
    equation_member = EquationMember()

    # Multiple terms with same degree
    equation_member.add(Term(value=1, degree=0))
    equation_member.add(Term(value=1, degree=2))
    equation_member.add(Term(value=1, degree=2))
    equation_member.add(Term(value=1, degree=2))
    equation_member.add(Term(value=1, degree=1))
    assert str(equation_member) == "X^2 + X^2 + X^2 + X + 1"

    equation_member.simplify()
    assert str(equation_member) == "3X^2 + X + 1"

    # With negative terms
    equation_member.clear()
    equation_member.add(Term(value=2, degree=1))
    equation_member.add(Term(value=-3, degree=1))
    equation_member.add(Term(value=1, degree=1))
    equation_member.simplify()
    assert str(equation_member) == "0"

    # Mixed degrees and signs
    equation_member.clear()
    equation_member.add(Term(value=3, degree=2))
    equation_member.add(Term(value=-1, degree=2))
    equation_member.add(Term(value=2, degree=1))
    equation_member.add(Term(value=4, degree=1))
    equation_member.add(Term(value=-1, degree=0))
    equation_member.add(Term(value=5, degree=0))
    equation_member.simplify()
    assert str(equation_member) == "2X^2 + 6X + 4"


def test_equation_member_get_sorted_terms():
    """Test internal _get_sorted_terms method"""
    equation_member = EquationMember()
    equation_member.add(Term(value=1, degree=0))
    equation_member.add(Term(value=1, degree=2))
    equation_member.add(Term(value=1, degree=1))

    sorted_terms = equation_member._get_sorted_terms()
    degrees = [term[0] for term in sorted_terms]
    assert degrees == [2, 1, 0]  # Descending order


def test_equation_init():
    """Test Equation initialization"""
    equation = Equation()
    assert isinstance(equation.left_member, EquationMember)
    assert isinstance(equation.right_member, EquationMember)
    assert str(equation.left_member) == "0"
    assert str(equation.right_member) == "0"


def test_equation_add_terms():
    """Test adding terms to equation sides"""
    equation = Equation()

    # Add to left member
    term1 = Term(value=2, degree=2)
    equation.add_to_left_member(term1)
    assert 2 in equation.left_member.terms

    # Add to right member
    term2 = Term(value=3, degree=1)
    equation.add_to_right_member(term2)
    assert 1 in equation.right_member.terms


def test_equation_str_empty():
    """Test string representation of empty equation"""
    equation = Equation()
    assert str(equation) == "0 = 0"


def test_equation_str_left_only():
    """Test string representation with only left side"""
    equation = Equation()
    equation.add_to_left_member(Term(value=1, degree=0))
    equation.add_to_left_member(Term(value=1, degree=2))
    equation.add_to_left_member(Term(value=1, degree=1))
    assert str(equation) == "X^2 + X + 1 = 0"


def test_equation_str_both_sides():
    """Test string representation with both sides"""
    equation = Equation()
    equation.add_to_left_member(Term(value=1, degree=0))
    equation.add_to_left_member(Term(value=1, degree=2))
    equation.add_to_left_member(Term(value=1, degree=1))

    equation.add_to_right_member(Term(value=1, degree=1))
    equation.add_to_right_member(Term(value=1, degree=2))
    equation.add_to_right_member(Term(value=1, degree=0))
    equation.add_to_right_member(Term(value=1, degree=1))
    assert str(equation) == "X^2 + X + 1 = X^2 + X + X + 1"


def test_equation_str_complex():
    """Test string representation with complex equation"""
    equation = Equation()

    # Left side: 2X^2 - 3X + 1
    equation.add_to_left_member(Term(value=2, degree=2))
    equation.add_to_left_member(Term(value=-3, degree=1))
    equation.add_to_left_member(Term(value=1, degree=0))

    # Right side: X^2 + 2X - 4
    equation.add_to_right_member(Term(value=1, degree=2))
    equation.add_to_right_member(Term(value=2, degree=1))
    equation.add_to_right_member(Term(value=-4, degree=0))

    assert str(equation) == "2X^2 - 3X + 1 = X^2 + 2X - 4"


def test_equation_with_decimal_coefficients():
    """Test equation with decimal coefficients"""
    equation = Equation()
    equation.add_to_left_member(Term(value=2.5, degree=2))
    equation.add_to_left_member(Term(value=-1.75, degree=1))
    equation.add_to_right_member(Term(value=3.14, degree=0))

    assert str(equation) == "2.5X^2 - 1.75X = 3.14"
