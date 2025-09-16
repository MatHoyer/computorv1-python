try:
    from .classes.Equation import Equation
    from .classes.Term import Term
except ImportError:
    from classes.Equation import Equation
    from classes.Term import Term


def get_equation_degree(equation: Equation):
    return max(equation.left_member.terms.keys())


def resolve_second_degree_equation(equation: Equation):
    a = equation.left_member.terms[2][0].get_value()
    b = equation.left_member.terms[1][0].get_value()
    c = equation.left_member.terms[0][0].get_value()
    term_a = Term(value=a, degree=0)
    term_b = Term(value=b, degree=0)
    term_c = Term(value=c, degree=0)

    delta = b ** 2 - 4 * a * c
    delta_term = Term(value=delta, degree=0)

    print("Discriminant calculation:", f"{term_b} ** 2 - 4 * {term_a} * {term_c} = {delta_term}")

    if delta == 0:
        print("Discriminant is 0, there is one solution")
    elif delta < 0:
        print("Discriminant is strictly negative, there are two complex solutions")
    else:
        print("Discriminant is strictly positive, there are two solutions")


def resolve_first_degree_equation(equation: Equation):
    degree_zero_term = equation.left_member.terms[0][0]
    equation.swap_term(degree_zero_term, to="right")
    print("Swapping degree zero term to right:", equation)

    degree_one_term = equation.left_member.terms[1][0]
    divider = Term(value=degree_one_term.get_value(), degree=0)
    equation.left_member.divide(divider)
    equation.right_member.divide(divider)
    print(f"Dividing by degree one term value ({divider}):", equation)


def resolve_zero_degree_equation(equation: Equation):
    if str(equation.left_member) == str(equation.right_member):
        print("Any real number is a solution")
    else:
        print("No solution")


def solve_equation(equation: Equation):
    print("Cleaned equation:", equation, end="\n\n")
    equation.left_member.simplify()
    equation.right_member.simplify()
    print("Simplified left member:", equation.left_member)
    print("Simplified right member:", equation.right_member, end="\n\n")

    print("Simplified equation:", equation)

    terms_to_swap = list(equation.right_member.terms.values())
    for term in terms_to_swap:
        for t in term:
            equation.swap_term(t, to="left")
    equation.right_member.clear()

    print("Pass all terms to left member:", equation, end="\n\n")
    equation.left_member.simplify()
    print("Simplified left member:", equation.left_member, end="\n\n")
    print("Simplified equation:", equation)
    degree = get_equation_degree(equation)

    match degree:
        case 2:
            print("Equation degree: 2")
            resolve_second_degree_equation(equation)
        case 1:
            print("Equation degree: 1")
            resolve_first_degree_equation(equation)
        case 0:
            print("Equation degree: 0")
            resolve_zero_degree_equation(equation)
        case _:
            print("The equation is of degree (", degree, ") is not supported")
            exit(1)
