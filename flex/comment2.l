STRING [a-zA-Z]+
%%
"/*"([^*]|"*"+[^*/])*"*"*"*/" ;
[ \t\n]+ ;
{STRING} { printf("String is %s\n", yytext); }
%%