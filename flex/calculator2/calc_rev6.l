%{
#include "calc_rev6.tab.h"
%}
%%
[0-9]*\.[0-9]+ 	{ 
    yylval.dval.tag = 1;
    yylval.dval.fval = atof(yytext); 
    return NUMBER; 
}
[0-9]+ {
    yylval.dval.tag = 0;
    yylval.dval.ival = atoi(yytext);
    return NUMBER;
}
[\t ] 	;
[a-z]	{ 
		yylval.ival = yytext[0] - 'a'; 
		return NAME; 
	}
"$" 	return 0;
\n	|
.	return yytext[0];
%%
