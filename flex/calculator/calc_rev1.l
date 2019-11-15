%{
#include "calc_rev1.tab.h"
%}
%%
[0-9]+  { yylval = atoi(yytext); return NUMBER; }
[\t]    ;
\n      return 0;
.       return yytext[0];
%%
