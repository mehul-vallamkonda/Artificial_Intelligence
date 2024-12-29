from sympy.logic.boolalg import to_cnf, And, Or, Not
from sympy import symbols

# Function to convert FOL to CNF
def fol_to_cnf(fof):
    # Convert to CNF
    cnf_expr = to_cnf(fof, True)
    return cnf_expr

# Example: A formula in FOL (you can replace this with your own FOL expression)
# (P(x) -> Q(x)) & (R(x) & S(x))

# Define the symbolic variables
P, Q, R, S = symbols('P Q R S')

# Formula (P -> Q) is equivalent to (~P | Q)
expr1 = Or(Not(P), Q) & And(R, S)

# Convert to CNF
cnf = fol_to_cnf(expr1)
print(f"CNF of the given FOL formula: {cnf}")
