

%{
#include <stdio.h>
#include <string.h>
%}

%%
if        { printf("Keyword: if\n"); }
else      { printf("Keyword: else\n"); }
int       { printf("Keyword: int\n"); }
float     { printf("Keyword: float\n"); }
[a-zA-Z][a-zA-Z0-9]*  { printf("Identifier: %s\n", yytext); }
[0-9]+    { printf("Number: %s\n", yytext); }
"+"|"-"|"*"|"/" { printf("Operator: %s\n", yytext); }
[ \t\n]+  { /* Ignore whitespace */ }
.         { printf("Unknown: %s\n", yytext); }
%%

int main() {
    yylex();  // Call the lexical analyzer
    return 0;
}


# Save the LEX Program: Save the code in a file named lexer.l.

# Generate C Code: Run the following command in the terminal to generate the C source code for the lexical analyzer:


# lex lexer.l
# Compile the C Code: After generating the C code (lex.yy.c), compile it using gcc:


# gcc lex.yy.c -o lexer -ll
# This will generate an executable named lexer.

# Run the Lexical Analyzer: Finally, you can test the lexical analyzer by providing it with an input file or direct input:


# ./lexer < input.txt
# Or run it interactively:


# ./lexer
# Example Input:
# For the input:


# int a = 5;
# float b = 3.14;
# if (a > b) {
#     printf("a is greater");
# }
#