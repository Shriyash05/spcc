from collections import defaultdict

# Sample grammar: G = { A → aB | ε, B → b | ε }
grammar = {
    'A': ['aB', 'ε'],
    'B': ['b', 'ε']
}

first_sets = defaultdict(set)

def compute_first(symbol):
    # Terminal
    if not symbol.isupper():
        return {symbol}

    # If already computed
    if symbol in first_sets and first_sets[symbol]:
        return first_sets[symbol]

    for production in grammar[symbol]:
        if production == 'ε':
            first_sets[symbol].add('ε')
        else:
            for i, char in enumerate(production):
                char_first = compute_first(char)

                # Add everything except epsilon
                first_sets[symbol].update(char_first - {'ε'})

                if 'ε' not in char_first:
                    break
                # If all chars produce ε, then add ε
                if i == len(production) - 1:
                    first_sets[symbol].add('ε')
    
    return first_sets[symbol]

# Compute FIRST sets
for non_terminal in grammar:
    compute_first(non_terminal)

# Print results
print("FIRST sets:")
for nt, first in first_sets.items():
    print(f"FIRST({nt}) = {{ {', '.join(first)} }}")
