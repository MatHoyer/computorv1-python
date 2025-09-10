from src.classes.Term import Term
import pytest


def test_term_str():
    term = Term(value=1, degree=2)
    term2 = Term(value=1, degree=1)
    term3 = Term(value=1, degree=0)
    term4 = Term(value=-1, degree=2)
    term5 = Term(value=-1, degree=1)
    term6 = Term(value=-1, degree=0)
    term7 = Term(value=0, degree=2)
    term8 = Term(value=0, degree=1)
    term9 = Term(value=0, degree=0)
    term10 = Term(value=2, degree=2)
    term11 = Term(value=2, degree=1.5)

    assert str(term) == "X^2"
    assert str(term2) == "X"
    assert str(term3) == "1"
    assert str(term4) == "-X^2"
    assert str(term5) == "-X"
    assert str(term6) == "-1"
    assert str(term7) == "0"
    assert str(term8) == "0"
    assert str(term9) == "0"
    assert str(term10) == "2X^2"
    assert str(term11) == "2X^1.5"


def test_term_get_str_signed():
    term = Term(value=1, degree=2)
    term2 = Term(value=1, degree=1)
    term3 = Term(value=1, degree=0)
    term4 = Term(value=-1, degree=2)
    term5 = Term(value=-1, degree=1)
    term6 = Term(value=-1, degree=0)
    term7 = Term(value=0, degree=2)
    term8 = Term(value=0, degree=1)
    term9 = Term(value=0, degree=0)
    term10 = Term(value=2, degree=2)
    term11 = Term(value=2, degree=1.5)

    assert term.get_str_signed() == "+ X^2"
    assert term2.get_str_signed() == "+ X"
    assert term3.get_str_signed() == "+ 1"
    assert term4.get_str_signed() == "- X^2"
    assert term5.get_str_signed() == "- X"
    assert term6.get_str_signed() == "- 1"
    assert term7.get_str_signed() == "+ 0"
    assert term8.get_str_signed() == "+ 0"
    assert term9.get_str_signed() == "+ 0"
    assert term10.get_str_signed() == "+ 2X^2"
    assert term11.get_str_signed() == "+ 2X^1.5"


def test_term_opposite():
    term = Term(value=1, degree=2)
    term2 = Term(value=-1, degree=1)
    term3 = Term(value=0, degree=3)

    assert term.opposite() == Term(value=-1, degree=2)
    assert term2.opposite() == Term(value=1, degree=1)
    assert term3.opposite() == Term(value=0, degree=3)


def test_term_absolute():
    term = Term(value=1, degree=2)
    term2 = Term(value=-1, degree=1)
    term3 = Term(value=0, degree=3)

    assert term.absolute() == Term(value=1, degree=2)
    assert term2.absolute() == Term(value=1, degree=1)
    assert term3.absolute() == Term(value=0, degree=3)


def test_term_add():
    term = Term(value=1, degree=2)
    term2 = Term(value=1, degree=2)
    term3 = Term(value=1, degree=1)
    term4 = Term(value=1, degree=2)

    assert term + term2 == Term(value=2, degree=2)
    with pytest.raises(NotImplementedError):
        term + term3
    assert term + term2 + term4 == Term(value=3, degree=2)


def test_term_sub():
    term = Term(value=1, degree=2)
    term2 = Term(value=1, degree=2)
    term3 = Term(value=1, degree=1)
    term4 = Term(value=1, degree=2)

    assert term - term2 == Term(value=0, degree=2)
    with pytest.raises(NotImplementedError):
        term - term3
    assert term - term2 - term4 == Term(value=-1, degree=2)


def test_term_mul():
    term = Term(value=1, degree=2)
    term2 = Term(value=1, degree=1)
    term3 = Term(value=1, degree=0)

    assert term * term2 == Term(value=1, degree=3)
    assert term * term3 == Term(value=1, degree=2)
    assert term2 * term3 == Term(value=1, degree=1)
    assert term * term2 * term3 == Term(value=1, degree=3)


def test_term_truediv():
    term = Term(value=1, degree=2)
    term2 = Term(value=1, degree=1)
    term3 = Term(value=1, degree=0)

    assert term / term2 == Term(value=1, degree=1)
    assert term / term3 == Term(value=1, degree=2)
    assert term2 / term3 == Term(value=1, degree=1)
    assert term / term2 / term3 == Term(value=1, degree=1)


def test_term_eq():
    term = Term(value=1, degree=2)
    term2 = Term(value=1, degree=1)
    term3 = Term(value=1, degree=0)
    term4 = Term(value=1, degree=2)

    assert term != term2
    assert term != term3
    assert term == term4
    assert term2 != term3
    assert term2 != term4
    assert term3 != term4
