from src.classes.Term import Term, format_float
import pytest


def test_format_float():
    """Test format_float utility function"""
    assert format_float(1.0) == 1
    assert format_float(2.5) == 2.5
    assert format_float(-3.0) == -3
    assert format_float(0.0) == 0
    assert format_float(1.25) == 1.25


def test_term_init():
    """Test Term initialization"""
    # Default degree
    term = Term(value=5)
    assert term.value == 5
    assert term.degree == 1
    assert term.sign == 1

    # Positive value
    term = Term(value=3, degree=2)
    assert term.value == 3
    assert term.degree == 2
    assert term.sign == 1

    # Negative value
    term = Term(value=-3, degree=2)
    assert term.value == 3  # absolute value
    assert term.degree == 2
    assert term.sign == -1

    # Zero value
    term = Term(value=0, degree=1)
    assert term.value == 0
    assert term.degree == 1
    assert term.sign == 1


def test_term_str_constant_terms():
    """Test string representation of constant terms (degree 0)"""
    assert str(Term(value=1, degree=0)) == "1"
    assert str(Term(value=-1, degree=0)) == "-1"
    assert str(Term(value=0, degree=0)) == "0"
    assert str(Term(value=5, degree=0)) == "5"
    assert str(Term(value=-3, degree=0)) == "-3"
    assert str(Term(value=2.5, degree=0)) == "2.5"
    assert str(Term(value=-1.75, degree=0)) == "-1.75"


def test_term_str_linear_terms():
    """Test string representation of linear terms (degree 1)"""
    assert str(Term(value=1, degree=1)) == "x"
    assert str(Term(value=-1, degree=1)) == "-x"
    assert str(Term(value=0, degree=1)) == "0"
    assert str(Term(value=2, degree=1)) == "2x"
    assert str(Term(value=-3, degree=1)) == "-3x"
    assert str(Term(value=2.5, degree=1)) == "2.5x"
    assert str(Term(value=-1.75, degree=1)) == "-1.75x"


def test_term_str_quadratic_terms():
    """Test string representation of quadratic terms (degree 2)"""
    assert str(Term(value=1, degree=2)) == "x²"
    assert str(Term(value=-1, degree=2)) == "-x²"
    assert str(Term(value=0, degree=2)) == "0"
    assert str(Term(value=2, degree=2)) == "2x²"
    assert str(Term(value=-3, degree=2)) == "-3x²"
    assert str(Term(value=2.5, degree=2)) == "2.5x²"


def test_term_str_higher_degree_terms():
    """Test string representation of higher degree terms"""
    assert str(Term(value=1, degree=3)) == "x³"
    assert str(Term(value=2, degree=1.5)) == "2x¹⋅⁵"
    assert str(Term(value=-1, degree=5)) == "-x⁵"
    assert str(Term(value=3, degree=0.5)) == "3x⁰⋅⁵"


def test_term_str_zero_value():
    """Test string representation when value is zero"""
    # Zero with any degree should return "0"
    assert str(Term(value=0, degree=0)) == "0"
    assert str(Term(value=0, degree=1)) == "0"
    assert str(Term(value=0, degree=2)) == "0"
    assert str(Term(value=0, degree=10)) == "0"


def test_term_repr():
    """Test __repr__ method"""
    term = Term(value=2, degree=3)
    assert repr(term) == str(term)
    assert repr(term) == "2x³"


def test_term_get_str_signed_positive():
    """Test get_str_signed for positive terms"""
    assert Term(value=1, degree=2).get_str_signed() == "+ x²"
    assert Term(value=1, degree=1).get_str_signed() == "+ x"
    assert Term(value=1, degree=0).get_str_signed() == "+ 1"
    assert Term(value=2, degree=2).get_str_signed() == "+ 2x²"
    assert Term(value=3, degree=1).get_str_signed() == "+ 3x"
    assert Term(value=5, degree=0).get_str_signed() == "+ 5"


def test_term_get_str_signed_negative():
    """Test get_str_signed for negative terms"""
    assert Term(value=-1, degree=2).get_str_signed() == "- x²"
    assert Term(value=-1, degree=1).get_str_signed() == "- x"
    assert Term(value=-1, degree=0).get_str_signed() == "- 1"
    assert Term(value=-2, degree=2).get_str_signed() == "- 2x²"
    assert Term(value=-3, degree=1).get_str_signed() == "- 3x"
    assert Term(value=-5, degree=0).get_str_signed() == "- 5"


def test_term_get_str_signed_zero():
    """Test get_str_signed for zero terms"""
    assert Term(value=0, degree=2).get_str_signed() == "+ 0"
    assert Term(value=0, degree=1).get_str_signed() == "+ 0"
    assert Term(value=0, degree=0).get_str_signed() == "+ 0"


def test_term_get_str_signed_decimal():
    """Test get_str_signed for decimal values"""
    assert Term(value=2.5, degree=2).get_str_signed() == "+ 2.5x²"
    assert Term(value=-1.75, degree=1).get_str_signed() == "- 1.75x"
    assert Term(value=3.14, degree=0).get_str_signed() == "+ 3.14"


def test_term_opposite():
    """Test opposite method"""
    # Positive to negative
    assert Term(value=1, degree=2).opposite() == Term(value=-1, degree=2)
    assert Term(value=3, degree=1).opposite() == Term(value=-3, degree=1)
    assert Term(value=5, degree=0).opposite() == Term(value=-5, degree=0)

    # Negative to positive
    assert Term(value=-1, degree=2).opposite() == Term(value=1, degree=2)
    assert Term(value=-3, degree=1).opposite() == Term(value=3, degree=1)
    assert Term(value=-5, degree=0).opposite() == Term(value=5, degree=0)

    # Zero stays zero
    assert Term(value=0, degree=3).opposite() == Term(value=0, degree=3)

    # Decimal values
    assert Term(value=2.5, degree=2).opposite() == Term(value=-2.5, degree=2)
    assert Term(value=-1.75, degree=1).opposite() == Term(value=1.75, degree=1)


def test_term_absolute():
    """Test absolute method"""
    # Already positive
    assert Term(value=1, degree=2).absolute() == Term(value=1, degree=2)
    assert Term(value=3, degree=1).absolute() == Term(value=3, degree=1)
    assert Term(value=5, degree=0).absolute() == Term(value=5, degree=0)

    # Negative to positive
    assert Term(value=-1, degree=2).absolute() == Term(value=1, degree=2)
    assert Term(value=-3, degree=1).absolute() == Term(value=3, degree=1)
    assert Term(value=-5, degree=0).absolute() == Term(value=5, degree=0)

    # Zero stays zero
    assert Term(value=0, degree=3).absolute() == Term(value=0, degree=3)

    # Decimal values
    assert Term(value=-2.5, degree=2).absolute() == Term(value=2.5, degree=2)


def test_term_add_same_degree():
    """Test addition with same degree"""
    # Positive + Positive
    assert Term(value=1, degree=2) + Term(value=1, degree=2) == Term(value=2, degree=2)
    assert Term(value=3, degree=1) + Term(value=2, degree=1) == Term(value=5, degree=1)

    # Positive + Negative
    assert Term(value=3, degree=2) + Term(value=-1, degree=2) == Term(value=2, degree=2)
    assert Term(value=2, degree=1) + Term(value=-2, degree=1) == Term(value=0, degree=1)

    # Negative + Negative
    assert Term(value=-1, degree=2) + Term(value=-2, degree=2) == Term(value=-3, degree=2)

    # Multiple additions
    result = Term(value=1, degree=2) + Term(value=1, degree=2) + Term(value=1, degree=2)
    assert result == Term(value=3, degree=2)

    # Decimal values
    assert Term(value=2.5, degree=1) + Term(value=1.5, degree=1) == Term(value=4.0, degree=1)


def test_term_add_different_degree():
    """Test addition with different degrees should raise error"""
    with pytest.raises(NotImplementedError, match="Terms must have the same degree to add"):
        Term(value=1, degree=2) + Term(value=1, degree=1)

    with pytest.raises(NotImplementedError):
        Term(value=1, degree=0) + Term(value=1, degree=3)


def test_term_sub_same_degree():
    """Test subtraction with same degree"""
    # Positive - Positive
    assert Term(value=3, degree=2) - Term(value=1, degree=2) == Term(value=2, degree=2)
    assert Term(value=1, degree=2) - Term(value=1, degree=2) == Term(value=0, degree=2)

    # Positive - Negative
    assert Term(value=1, degree=2) - Term(value=-2, degree=2) == Term(value=3, degree=2)

    # Negative - Positive
    assert Term(value=-1, degree=2) - Term(value=2, degree=2) == Term(value=-3, degree=2)

    # Multiple subtractions
    result = Term(value=1, degree=2) - Term(value=1, degree=2) - Term(value=1, degree=2)
    assert result == Term(value=-1, degree=2)

    # Decimal values
    assert Term(value=3.5, degree=1) - Term(value=1.5, degree=1) == Term(value=2.0, degree=1)


def test_term_sub_different_degree():
    """Test subtraction with different degrees should raise error"""
    with pytest.raises(NotImplementedError, match="Terms must have the same degree to subtract"):
        Term(value=1, degree=2) - Term(value=1, degree=1)

    with pytest.raises(NotImplementedError):
        Term(value=1, degree=0) - Term(value=1, degree=3)


def test_term_mul():
    """Test multiplication"""
    # Basic multiplication
    assert Term(value=1, degree=2) * Term(value=1, degree=1) == Term(value=1, degree=3)
    assert Term(value=1, degree=2) * Term(value=1, degree=2) == Term(value=1, degree=4)
    assert Term(value=1, degree=1) * Term(value=1, degree=2) == Term(value=1, degree=3)

    # With coefficients
    assert Term(value=2, degree=1) * Term(value=3, degree=2) == Term(value=6, degree=3)
    assert Term(value=-2, degree=1) * Term(value=3, degree=2) == Term(value=-6, degree=3)
    assert Term(value=-2, degree=1) * Term(value=-3, degree=2) == Term(value=6, degree=3)

    # With zero degree
    assert Term(value=2, degree=0) * Term(value=3, degree=1) == Term(value=6, degree=1)
    assert Term(value=5, degree=2) * Term(value=2, degree=0) == Term(value=10, degree=2)

    # Decimal values
    assert Term(value=2.5, degree=1) * Term(value=2, degree=2) == Term(value=5.0, degree=3)


def test_term_truediv():
    """Test division"""
    # Basic division
    assert Term(value=1, degree=2) / Term(value=1, degree=3) == Term(value=1, degree=-1)
    assert Term(value=1, degree=2) / Term(value=1, degree=2) == Term(value=1, degree=0)
    assert Term(value=1, degree=3) / Term(value=1, degree=2) == Term(value=1, degree=1)

    # With coefficients
    assert Term(value=6, degree=3) / Term(value=2, degree=1) == Term(value=3, degree=2)
    assert Term(value=8, degree=2) / Term(value=4, degree=1) == Term(value=2, degree=1)

    # Negative values
    assert Term(value=-6, degree=3) / Term(value=2, degree=1) == Term(value=-3, degree=2)
    assert Term(value=6, degree=3) / Term(value=-2, degree=1) == Term(value=-3, degree=2)

    # Decimal values
    assert Term(value=5.0, degree=3) / Term(value=2.5, degree=1) == Term(value=2.0, degree=2)


def test_term_eq():
    """Test equality comparison"""
    # Equal terms
    assert Term(value=1, degree=2) == Term(value=1, degree=2)
    assert Term(value=-3, degree=1) == Term(value=-3, degree=1)
    assert Term(value=0, degree=0) == Term(value=0, degree=0)
    assert Term(value=2.5, degree=1.5) == Term(value=2.5, degree=1.5)

    # Different values
    assert Term(value=1, degree=2) != Term(value=2, degree=2)
    assert Term(value=1, degree=2) != Term(value=-1, degree=2)

    # Different degrees
    assert Term(value=1, degree=2) != Term(value=1, degree=1)
    assert Term(value=1, degree=0) != Term(value=1, degree=3)

    # Different signs
    assert Term(value=1, degree=2) != Term(value=-1, degree=2)
    assert Term(value=-1, degree=1) != Term(value=1, degree=1)


def test_term_edge_cases():
    """Test edge cases and special values"""
    # Very small values
    term = Term(value=0.001, degree=1)
    assert term.value == 0.001
    assert term.sign == 1

    # Very large values
    term = Term(value=1000000, degree=10)
    assert term.value == 1000000
    assert term.degree == 10

    # Fractional degrees
    term = Term(value=2, degree=0.5)
    assert str(term) == "2x⁰⋅⁵"

    # Negative degrees
    term = Term(value=1, degree=-1)
    assert str(term) == "x⁻¹"

    # Complex operations
    term1 = Term(value=0.5, degree=2.5)
    term2 = Term(value=2, degree=1.5)
    result = term1 * term2
    assert result.value == 1.0
    assert result.degree == 4.0
