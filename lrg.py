def remove_left_recursion(non_terminal, productions):
    alpha = []  # Left-recursive parts (A → Aα)
    beta = []   # Non-left-recursive parts (A → β)

    for prod in productions:
        if prod.startswith(non_terminal):
            alpha.append(prod[len(non_terminal):])
        else:
            beta.append(prod)

    if not alpha:
        print(f"{non_terminal} → {' | '.join(productions)}  # No left recursion")
        return

    # Create new non-terminal
    new_nt = non_terminal + "'"

    # A → βA'
    new_prods_A = [b + new_nt for b in beta]

    # A' → αA' | ε
    new_prods_A_dash = [a + new_nt for a in alpha]
    new_prods_A_dash.append('ε')  # epsilon

    print(f"{non_terminal} → {' | '.join(new_prods_A)}")
    print(f"{new_nt} → {' | '.join(new_prods_A_dash)}")


# Example: Replace with your own input
non_terminal = "A"
productions = ["Aa", "b", "c", "Ad"]

remove_left_recursion(non_terminal, productions)


