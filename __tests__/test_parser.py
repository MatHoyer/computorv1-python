from src.parser import parse_equation


def test_parse_equation():
    # Test cases with different signs
    equation = parse_equation("-X^2 + 3X - 2 = 0")
    assert str(equation) == "-x² + 3x - 2 = 0"

    equation = parse_equation("X^2 - 5X + 6 = 0")
    assert str(equation) == "x² - 5x + 6 = 0"

    # Test cases with decimal coefficients
    equation = parse_equation("2.5X^2 + 1.5X - 3.7 = 0")
    assert str(equation) == "2.5x² + 1.5x - 3.7 = 0"

    # Test cases with single terms
    equation = parse_equation("X = 0")
    assert str(equation) == "x = 0"

    equation = parse_equation("5 = 0")
    assert str(equation) == "5 = 0"

    equation = parse_equation("X^3 = 0")
    assert str(equation) == "x³ = 0"

    # Test cases with zero coefficients
    equation = parse_equation("0X^2 + X + 1 = 0")
    assert str(equation) == "0 + x + 1 = 0"

    # Test cases with complex equations
    equation = parse_equation("X^2 + 2X + 1 = X^2 + 2X + 1")
    assert str(equation) == "x² + 2x + 1 = x² + 2x + 1"

    equation = parse_equation("3X^4 - 2X^3 + X^2 - X + 1 = 5X^4 + 3X^3 - 2X^2 + 4X - 7")
    assert str(equation) == "3x⁴ - 2x³ + x² - x + 1 = 5x⁴ + 3x³ - 2x² + 4x - 7"

    # Test cases with implicit coefficients
    equation = parse_equation("X^2 + X = 0")
    assert str(equation) == "x² + x = 0"

    equation = parse_equation("-X^2 - X = 0")
    assert str(equation) == "-x² - x = 0"

    # Test cases with spaces and multiplication signs
    equation = parse_equation("X^2 + 2*X + 1 = 0")
    assert str(equation) == "x² + 2x + 1 = 0"

    equation = parse_equation("  X^2  +  X  +  1  =  0  ")
    assert str(equation) == "x² + x + 1 = 0"

    # Test cases with only constants
    equation = parse_equation("5 = 3")
    assert str(equation) == "5 = 3"

    equation = parse_equation("0 = 0")
    assert str(equation) == "0 = 0"

    # Test cases with mixed terms
    equation = parse_equation("X^2 + 1 = X + 1")
    assert str(equation) == "x² + 1 = x + 1"

    equation = parse_equation("2X^3 - X^2 + 3X - 1 = X^3 + 2X^2 - X + 4")
    assert str(equation) == "2x³ - x² + 3x - 1 = x³ + 2x² - x + 4"

    # Test cases with fractional coefficients
    equation = parse_equation("0.5X^2 + 0.25X - 0.75 = 0")
    assert str(equation) == "0.5x² + 0.25x - 0.75 = 0"

    # Test cases with very large degrees
    equation = parse_equation("X^10 + X^5 + 1 = 0")
    assert str(equation) == "x¹⁰ + x⁵ + 1 = 0"

    # Test cases with negative coefficients
    equation = parse_equation("-2X^2 - 3X - 4 = 0")
    assert str(equation) == "-2x² - 3x - 4 = 0"

    # Test cases with zero terms
    equation = parse_equation("X^2 + 0X + 1 = 0")
    assert str(equation) == "x² + 0 + 1 = 0"

    # Test cases with complex right side
    equation = parse_equation("0 = X^2 + X + 1")
    assert str(equation) == "0 = x² + x + 1"

    # Test cases with multiple terms of same degree (should be handled by simplify)
    equation = parse_equation("X^2 + X^2 + X = 0")
    # Note: This will need simplify() to be called to combine like terms
    equation.left_member.simplify()
    assert str(equation) == "2x² + x = 0"
