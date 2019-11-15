
%%
"const"	{ ECHO; printf(" "); }
"var"	{ ECHO; printf(" "); }
"procedure"	{ ECHO; printf(" "); }
":="	{ ECHO; printf(" "); }
","	{ ECHO; printf(" "); }
";"	{ ECHO; printf(" "); }
"="	{ ECHO; printf(" "); }
"while"	{ ECHO; printf(" "); }
"do"	{ ECHO; printf(" "); }
"begin"	{ ECHO; printf(" "); }
"end"	{ ECHO; printf(" "); }
"if"	{ ECHO; printf(" "); }
"odd"	{ ECHO; printf(" "); }
"call" { ECHO; printf(" "); }

"+"	{ ECHO; printf(" "); }
"-"	{ ECHO; printf(" "); }
"*"	{ ECHO; printf(" "); }
"/"	{ ECHO; printf(" "); }
">"	{ ECHO; printf(" "); }
"<"	{ ECHO; printf(" "); }

[A-Za-z_][A-Za-z0-9_]* { ECHO; printf(" "); }
[1-9][0-9]*|0([0-7]+|(x|X)[0-9A-Fa-f]*)? { ECHO; printf(" "); }
"/*"([^*]|\*+[^*/])*\**"*/"	;
"//".*	;
[ \t\n ]	;
.	return(yytext[0]);

%%
