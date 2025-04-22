%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
void yyerror(const char *s);
%}

%token NUMBER

%%

calculation: expression '\n' { printf("Result = %d\n", $1); }
           ;

expression: expression '+' term { $$ = $1 + $3; }
          | expression '-' term { $$ = $1 - $3; }
          | term { $$ = $1; }
          ;

term: term '*' factor { $$ = $1 * $3; }
    | term '/' factor { $$ = $1 / $3; }
    | factor { $$ = $1; }
    ;

factor: NUMBER { $$ = atoi(yytext); }
       | '(' expression ')' { $$ = $2; }
       ;

%%

int main() {
    printf("Enter an expression: ");
    yyparse(); // Start parsing
    return 0;
}

void yyerror(const char *s) {
    printf("Error: %s\n", s);
}


#lex program to tokenize the input for yacc parser
%{
#include "y.tab.h"
%}

%%

[0-9]+      { yylval = atoi(yytext); return NUMBER; }
[ \t\n]+    { /* Ignore whitespace */ }
.           { return yytext[0]; }

%%

int yywrap() { return 1; }


# yacc -d calc.y
# lex calc.l
# gcc lex.yy.c y.tab.c -o calc -ll -ly
# ./calc
# 3 + 5 * (2 - 8)
# Result = -13 output