import sys
from classes.Equation import Equation
from classes.Term import Term

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print("Usage: python computor.py <equation>")
        sys.exit(1)

    eq = Equation()
    eq.add_to_member("left", Term(value=1, degree=1))
    eq.add_to_member("left", Term(value=1, degree=2))
    eq.add_to_member("left", Term(value=1, degree=0))
    eq.add_to_member("left", Term(value=1, degree=1))
    eq.add_to_member("right", Term(value=1, degree=1))
    eq.add_to_member("right", Term(value=1, degree=2))
    eq.add_to_member("right", Term(value=1, degree=0))
    eq.add_to_member("right", Term(value=1, degree=1))

    print(eq)
