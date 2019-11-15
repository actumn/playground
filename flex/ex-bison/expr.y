
/*
 * 영문법.y : Prsing for 영어문장
 */
%{
#include <stdio.h>
int ln = 1, cp = 0;
%}
%token NOUN PRONOUN VERB CONJUNCTION ADJECTIVE ADVERB PREPOSITION UNKNOWN
%%
Start: |
Start sentence '.' { printf(" ==== valid syntax ====\n"); }
;

sentence: subject VERB |
subject VERB object |
sentence CONJUNCTION sentence
;

subject: NOUN | PRONOUN
;

object: NOUN | NOUN PREPOSITION NOUN | ADJECTIVE | ADVERB ADJECTIVE
;


%%
void yyerror(char* s) {
 printf("line: %d cp: %d %s\n", ln, cp, s);
}
int main() {
 return yyparse();
}
