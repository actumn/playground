%{
#include <stdio.h>
%}
%token NOUN VERB PRONOUN ADJECTIVE
%%
sentence : subject VERB object { printf("Sentence is valid.\n"); }
;

subject : NOUN | PRONOUN
;

object : NOUN | ADJECTIVE
;
%%
