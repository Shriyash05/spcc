from collections import defaultdict

# Sample grammar
grammar = {
    'S': ['AB'],
    'A': ['aA', 'ε'],
    'B': ['b']
}

first_sets = defaultdict(set)
follow_sets = defaultdict(set)
start_symbol = 'S'

# Compute FIRST of a symbol
def compute_first(symbol):
    if not symbol.isupper():  # terminal
        return {symbol}
    if symbol in first_sets and first_sets[symbol]:
        return first_sets[symbol]

    for production in grammar[symbol]:
        if production == 'ε':
            first_sets[symbol].add('ε')
        else:
            for i, char in enumerate(production):
                char_first = compute_first(char)
                first_sets[symbol].update(char_first - {'ε'})

                if 'ε' not in char_first:
                    break
                if i == len(production) - 1:
                    first_sets[symbol].add('ε')
    return first_sets[symbol]

# Compute all FIRST sets
for non_terminal in grammar:
    compute_first(non_terminal)

# Add $ to FOLLOW(start symbol)
follow_sets[start_symbol].add('$')

# Compute FOLLOW sets
def compute_follow():
    changed = True
    while changed:
        changed = False
        for head, productions in grammar.items():
            for production in productions:
                for i in range(len(production)):
                    B = production[i]
                    if B.isupper():
                        # Lookahead in production
                        after = production[i+1:]
                        if after:
                            # Compute FIRST(after)
                            first_of_after = set()
                            for j in range(len(after)):
                                f = compute_first(after[j])
                                first_of_after.update(f - {'ε'})
                                if 'ε' not in f:
                                    break
                                if j == len(after) - 1:
                                    first_of_after.add('ε')
                            # Add FIRST(after) - ε to FOLLOW(B)
                            if not first_of_after.issubset(follow_sets[B]):
                                follow_sets[B].update(first_of_after - {'ε'})
                                changed = True
                            # If ε in FIRST(after), add FOLLOW(head)
                            if 'ε' in first_of_after:
                                if not follow_sets[head].issubset(follow_sets[B]):
                                    follow_sets[B].update(follow_sets[head])
                                    changed = True
                        else:
                            # B is at end, add FOLLOW(head)
                            if not follow_sets[head].issubset(follow_sets[B]):
                                follow_sets[B].update(follow_sets[head])
                                changed = True

compute_follow()

# Print results
print("FOLLOW sets:")
for nt, follow in follow_sets.items():
    print(f"FOLLOW({nt}) = {{ {', '.join(follow)} }}")
