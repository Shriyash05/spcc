import re

# Define sets of different types of operators
arithmetic_operators = {'+', '-', '*', '/', '%'}
relational_operators = {'==', '!=', '>', '<', '>=', '<='}
logical_operators = {'&&', '||', '!'}
assignment_operators = {'=', '+=', '-=', '*=', '/='}

# Combine all operators into one set
all_operators = arithmetic_operators | relational_operators | logical_operators | assignment_operators

# Regex to split the input by whitespace and also keep operators
token_pattern = r'(\+\=|\-\=|\*\=|\/\=|\=\=|\!\=|\>\=|\<\=|\&\&|\|\||\+|\-|\*|\/|\%|\=|\>|\<|\!)'

def lexical_analyzer(input_code):
    # Split code using the operator regex while keeping the matched operators
    tokens = re.split(r'(\s+|' + token_pattern + r')', input_code)
    tokens = [tok for tok in tokens if tok and not tok.isspace()]

    print("Lexical Analysis Output:\n")
    for token in tokens:
        if token in arithmetic_operators:
            print(f"{token} ➝ Arithmetic Operator")
        elif token in relational_operators:
            print(f"{token} ➝ Relational Operator")
        elif token in logical_operators:
            print(f"{token} ➝ Logical Operator")
        elif token in assignment_operators:
            print(f"{token} ➝ Assignment Operator")
        else:
            print(f"{token} ➝ Not an Operator (Possibly Identifier / Number / Keyword)")

# Example input
code = "a = b + c * 2; if (a >= 10 && b != 5) d += 1;"

# Run lexical analyzer
lexical_analyzer(code)
