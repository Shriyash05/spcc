import re

# Define a list of keywords (You can expand this list)
keywords = [
    "if", "else", "while", "do", "break", "continue", "int",
    "float", "return", "char", "case", "sizeof", "long",
    "short", "typedef", "switch", "unsigned", "void", "static",
    "struct", "goto", "for", "const", "auto", "double"
]

# Regular expression for valid identifier
identifier_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'

def lexical_analyzer(input_code):
    tokens = input_code.split()
    print("Lexical Analysis Output:\n")
    for token in tokens:
        if token in keywords:
            print(f"{token} ➝ Keyword")
        elif re.match(identifier_pattern, token):
            print(f"{token} ➝ Identifier")
        else:
            print(f"{token} ➝ Unknown / Not an identifier or keyword")

# Example input
code = "int number = 10; float average; if (number > 0) return number;"

# Remove common separators and split cleanly
# cleaned_code = re.sub(r'[;(){}=><+*/,-]', ' ', code)

# Run lexical analyzer
lexical_analyzer(code)
