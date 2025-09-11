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
    assert Term(value=1, degree=2).get_str_signed() == "+ X^2"
    assert Term(value=1, degree=1).get_str_signed() == "+ X"
    assert Term(value=1, degree=0).get_str_signed() == "+ 1"
    assert Term(value=-1, degree=2).get_str_signed() == "- X^2"
    assert Term(value=-1, degree=1).get_str_signed() == "- X"
    assert Term(value=-1, degree=0).get_str_signed() == "- 1"
    assert Term(value=0, degree=2).get_str_signed() == "+ 0"
    assert Term(value=0, degree=1).get_str_signed() == "+ 0"
    assert Term(value=0, degree=0).get_str_signed() == "+ 0"
    assert Term(value=2, degree=2).get_str_signed() == "+ 2X^2"
    assert Term(value=2, degree=1.5).get_str_signed() == "+ 2X^1.5"


def test_term_opposite():
    assert Term(value=1, degree=2).opposite() == Term(value=-1, degree=2)
    assert Term(value=-1, degree=1).opposite() == Term(value=1, degree=1)
    assert Term(value=0, degree=3).opposite() == Term(value=0, degree=3)


def test_term_absolute():
    assert Term(value=1, degree=2).absolute() == Term(value=1, degree=2)
    assert Term(value=-1, degree=1).absolute() == Term(value=1, degree=1)
    assert Term(value=0, degree=3).absolute() == Term(value=0, degree=3)


def test_term_add():
    assert Term(value=1, degree=2) + Term(value=1, degree=2) == Term(value=2, degree=2)
    with pytest.raises(NotImplementedError):
        Term(value=1, degree=2) + Term(value=1, degree=1)
    assert Term(value=1, degree=2) + Term(value=1, degree=2) + Term(value=1, degree=2) == Term(value=3, degree=2)


def test_term_sub():
    assert Term(value=1, degree=2) - Term(value=1, degree=2) == Term(value=0, degree=2)
    with pytest.raises(NotImplementedError):
        Term(value=1, degree=2) - Term(value=1, degree=1)
    assert Term(value=1, degree=2) - Term(value=1, degree=2) - Term(value=1, degree=2) == Term(value=-1, degree=2)


def test_term_mul():
    assert Term(value=1, degree=2) * Term(value=1, degree=1) == Term(value=1, degree=3)
    assert Term(value=1, degree=2) * Term(value=1, degree=2) == Term(value=1, degree=4)
    assert Term(value=1, degree=1) * Term(value=1, degree=2) == Term(value=1, degree=3)


def test_term_truediv():
    assert Term(value=1, degree=2) / Term(value=1, degree=3) == Term(value=1, degree=-1)
    assert Term(value=1, degree=2) / Term(value=1, degree=2) == Term(value=1, degree=0)
    assert Term(value=1, degree=3) / Term(value=1, degree=2) == Term(value=1, degree=1)


def test_term_eq():
    assert Term(value=1, degree=2) != Term(value=-1, degree=2)
    assert Term(value=1, degree=2) == Term(value=1, degree=2)
    assert Term(value=1, degree=2) != Term(value=1, degree=1)
