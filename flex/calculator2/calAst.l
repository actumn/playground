%{
#include "myAst.h"
#include "calAst.tab.h"
%}
%option noyywrap
%%
[0-9]+	{ yylval.ival = atoi(yytext); return NUMBER; }
[\t ]	 ;
"$"	return 0;
\n |
.	return yytext[0];
%%
