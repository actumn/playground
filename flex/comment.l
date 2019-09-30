STRING [a-zA-Z]+
%%
"/*".*"*/" { ECHO; }
[ \t\n]+ ;
{STRING} { printf("String is %s\n", yytext); }
%%
