%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
void yyerror(const char *s);
%}

%token NUMBER

%%

expression: expression '+' term { $$ = $1 + $3; }
          | expression '-' term { $$ = $1 - $3; }
          | term                 { $$ = $1; }
          ;

term: term '*' factor { $$ = $1 * $3; }
    | term '/' factor { 
        if ($3 == 0) {
            yyerror("Error: Division by Zero");
            YYABORT;
        } 
        $$ = $1 / $3; 
    }
    | factor { $$ = $1; }
    ;

factor: NUMBER { $$ = atoi(yytext); }
       | '(' expression ')' { $$ = $2; }
       ;

%%

int main() {
    printf("Enter an arithmetic expression: ");
    yyparse();  // Start parsing
    return 0;
}

void yyerror(const char *s) {
    printf("Error: %s\n", s);
}


# lexer for this yacc
%{
#include "y.tab.h"
%}

%%

[0-9]+        { yylval = atoi(yytext); return NUMBER; }
[ \t\n]+      { /* Ignore whitespace */ }
.             { return yytext[0]; }

%%

int yywrap() {
    return 1;
}


# Save the YACC code in a file called eval.y and the LEX code in lexer.l.

# Generate the C Code for the parser:


# yacc -d eval.y
# Generate the LEX code:


# lex lexer.l
# Compile the C Code:


# gcc lex.yy.c y.tab.c -o calc -ll -ly
# Run the Calculator:


# ./calc
# Example Input:

# Enter an arithmetic expression: 3 + 5 * (2 - 8)
# Example Output:


# Result = -13
#