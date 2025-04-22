%{
#include <stdio.h>
#include <stdlib.h>
%}

%%

[0-9]+  {
            int num = atoi(yytext);  // Convert the matched text to an integer
            if (num % 2 == 0) {
                printf("Even: %d\n", num);
            } else {
                printf("Odd: %d\n", num);
            }
        }

[ \t\n]+  { /* Ignore spaces and newlines */ }

.  { printf("Invalid character: %s\n", yytext); }  // Handle invalid characters

%%

int main() {
    yylex();  // Call the lexical analyzer
    return 0;
}



# lex odd_even.l
# gcc lex.yy.c -o odd_even -ll
# ./odd_even OR echo "123 456 789" | ./odd_even
