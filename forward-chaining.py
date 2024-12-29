from sympy.logic.boolalg import Or, And, Not, Implies
from sympy import symbols

# Forward reasoning (forward chaining) implementation
def forward_reasoning(facts, rules, query):
    # Start with the facts
    known_facts = set(facts)

    # Loop until no new facts are derived
    new_facts = True
    while new_facts:
        new_facts = False
        for rule in rules:
            # Apply each rule if its premises are in known facts
            if all(premise in known_facts for premise in rule[0]):
                # Add conclusion to known facts
                if rule[1] not in known_facts:
                    known_facts.add(rule[1])
                    new_facts = True

    # Return whether the query is in the known facts
    return query in known_facts

# Define symbols (variables)
A, B, C, D = symbols('A B C D')

# Knowledge Base (KB)
facts = [A, B]  # Initial facts (we know A and B are true)

# Rules (Implications)
# (A -> C) means if A is true, then C must be true
# (B -> D) means if B is true, then D must be true
rules = [
    ([A], C),  # A -> C
    ([B], D)   # B -> D
]

# Query (We want to prove if C is true)
query = C

# Perform forward reasoning
result = forward_reasoning(facts, rules, query)

# Output the result
print(f"Can we prove that {query}? {'Yes' if result else 'No'}")
