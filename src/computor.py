import sys
from parser import parse_equation
from solver import solve_equation

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print("Usage: python computor.py <equation>")
        sys.exit(1)

    eq = parse_equation(args[0])
    solve_equation(eq)
