%{
#include "expr.tab.h"
extern int ln, cp;
%}
%option noyywrap
%%
"soccer" | 
"food" | 
"house" | 
"balls" 	{ cp += yyleng; return NOUN; }
"is" | 
"am" | 
"are" | 
"do" | 
"have" |
"go" | 
"play" { cp += yyleng; return VERB; }
"I" |
"you" |
"he" |
"she" | 
"we" | 
"they" { cp += yyleng; return PRONOUN; }

"kind" |
"happy" | 
"sad" | 
"gentle" { cp += yyleng; return ADJECTIVE; }
"very" | 
"gently" { cp += yyleng; return ADVERB; }
"in" | 
"on" | 
"of"  { cp += yyleng; return PREPOSITION; }
"and" | 
"or" | 
"that" { cp += yyleng; return CONJUNCTION; }
"."	{ cp += yyleng; return '.'; }

"the" |
"english" { return UNKNOWN; }

[\n]  { ln++; };

[ \t]* 	;    /* throw away whitespace */

[a-zA-Z]+ { yyerror("Illegal character");  }
%%
