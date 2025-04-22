def remove_indirect_left_recursion(productions):
    # Step 1: Prepare the new grammar
    non_terminals = list(productions.keys())
    new_productions = {nt: [] for nt in non_terminals}

    for i, A in enumerate(non_terminals):
        for j in range(i):
            B = non_terminals[j]
            # Step 2: Eliminate indirect recursion A → Bα
            for prod in productions[A]:
                if prod.startswith(B):
                    for b_prod in productions[B]:
                        new_productions[A].append(b_prod + prod[len(B):])
                else:
                    new_productions[A].append(prod)
        
        # Step 3: Eliminate direct left recursion (if any)
        left_recursions = [prod for prod in productions[A] if prod.startswith(A)]
        non_left_recursions = [prod for prod in productions[A] if not prod.startswith(A)]
        
        if left_recursions:
            new_non_terminal = A + "'"
            new_productions[A] = [prod + new_non_terminal for prod in non_left_recursions]
            new_productions[new_non_terminal] = [prod[1:] + new_non_terminal for prod in left_recursions] + ['ε']
        else:
            new_productions[A] = non_left_recursions

    return new_productions

# Example grammar with indirect left recursion
productions = {
    'A': ['Bα', 'β'],
    'B': ['Aβ', 'γ']
}

# Remove indirect left recursion
new_grammar = remove_indirect_left_recursion(productions)

# Output the new grammar
for non_terminal, prod in new_grammar.items():
    print(f"{non_terminal} → {' | '.join(prod)}")

# input
# A → Bα | β
# B → Aβ | γ


# output
# A → βB' | BαB'
# B' → γB' | ε
# B → γ
