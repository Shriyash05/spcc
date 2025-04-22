# Largest word

%{
#include <stdio.h>
#include <string.h>
%}

%%

[a-zA-Z]+ {
    if (strlen(yytext) > strlen(largest)) {
        strcpy(largest, yytext);
    }
}

%%

int main() {
    char largest[100] = "";
    yylex();
    printf("Largest word: %s\n", largest);
    return 0;
}

# prime
%{
#include <stdio.h>
#include <stdlib.h>

int is_prime(int num) {
    if (num <= 1) return 0;
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) return 0;
    }
    return 1;
}
%}

%%

[0-9]+ {
    int num = atoi(yytext);
    if (is_prime(num)) {
        printf("%d is Prime\n", num);
    } else {
        printf("%d is Not Prime\n", num);
    }
}

%%

int main() {
    yylex();
    return 0;
}


# vowels
%{
#include <stdio.h>
int count = 0;
%}

%%

[aeiouAEIOU] { count++; }

%%

int main() {
    yylex();
    printf("Vowels Count: %d\n", count);
    return 0;
}

# identifiers and keywords
%{
#include <stdio.h>
#include <string.h>
const char *keywords[] = {"if", "else", "while", "int", "float"};
int is_keyword(char *word) {
    for (int i = 0; i < 5; i++) {
        if (strcmp(word, keywords[i]) == 0) return 1;
    }
    return 0;
}
%}

%%

[a-zA-Z_][a-zA-Z0-9_]* {
    if (is_keyword(yytext)) {
        printf("Keyword: %s\n", yytext);
    } else {
        printf("Identifier: %s\n", yytext);
    }
}

%%

int main() {
    yylex();
    return 0;
}

# operator
%{
#include <stdio.h>
%}

%%

\+    { printf("Operator: +\n"); }
\-    { printf("Operator: -\n"); }
\*    { printf("Operator: *\n"); }
\/    { printf("Operator: /\n"); }
\=    { printf("Operator: =\n"); }
\>\=  { printf("Operator: >=\n"); }
\<\=  { printf("Operator: <=\n"); }
\>\   { printf("Operator: >\n"); }
\<    { printf("Operator: <\n"); }
\!    { printf("Operator: !\n"); }

%%

int main() {
    yylex();
    return 0;
}

# lex lexer.l
# gcc lex.yy.c -o lexer -ll
# ./lexer