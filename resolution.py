import itertools

# Function to negate a literal
def negate_literal(literal):
    if literal.startswith("¬"):
        return literal[1:]  # Remove negation
    else:
        return "¬" + literal  # Add negation

# Resolution function: resolves two clauses
def resolve_clause(clause1, clause2):
    resolved_clauses = set()
    for literal in clause1:
        if negate_literal(literal) in clause2:
            # Create a resolvent by removing the complementary literals
            resolvent = (clause1 - {literal}) | (clause2 - {negate_literal(literal)})
            resolved_clauses.add(frozenset(resolvent))
    return resolved_clauses

# Resolution algorithm
def resolution(knowledge_base, query):
    # Add the negated query to the knowledge base
    negated_query = {negate_literal(literal) for literal in query}
    clauses = knowledge_base + [frozenset(negated_query)]  # Ensure all clauses are frozensets
    new_clauses = set()

    print("\n--- Resolution Steps ---")
    while True:
        # Resolve each pair of clauses
        pairs = list(itertools.combinations(clauses, 2))
        for (clause1, clause2) in pairs:
            resolvents = resolve_clause(clause1, clause2)
            if frozenset() in resolvents:  # Empty clause found
                print(f"Resolving {clause1} and {clause2} yields an empty clause. Query proven!")
                return True
            new_clauses = new_clauses.union(resolvents)

        # If no new clauses are generated, query cannot be proven
        if all(resolvent in clauses for resolvent in new_clauses):
            print("No new clauses generated. Query cannot be proven.")
            return False

        # Add new clauses to the knowledge base
        clauses.extend(new_clauses)
        print(f"Newly derived clauses: {new_clauses}")

# Convert sentences to CNF manually
def convert_to_cnf(kb):
    # This function assumes KB is already in a simplified CNF-like format for ease of implementation.
    # Normally, sentences would need parsing and transformation into CNF.
    return [frozenset(clause.split(" ∨ ")) for clause in kb]

# Main function
def main():
    print("Propositional Logic - Resolution Proof System\n")
    
    # Knowledge base in propositional logic (CNF format)
    knowledge_base = [
        "H(j)",               # John is a human
        "¬H(x) ∨ M(x)",       # If someone is a human, they are mortal
        "H(m)",               # Mary is a human
        "¬M(m)",              # Mary is not mortal
    ]
    
    # Convert KB to CNF format
    kb_in_cnf = convert_to_cnf(knowledge_base)
    print("Knowledge Base (in CNF):")
    for clause in kb_in_cnf:
        print(" ∨ ".join(clause))
    
    # Query: Is John mortal?
    query = {"M(j)"}
    print("\nQuery:", " ∧ ".join(query))
    
    # Apply resolution
    result = resolution(kb_in_cnf, query)
    if result:
        print("\nThe query is proven using resolution.")
    else:
        print("\nThe query cannot be proven using resolution.")

if __name__ == "__main__":
    main()
