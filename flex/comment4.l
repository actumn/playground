%{
int level=0;
%}
%x     CMNT
STRING [a-zA-Z]+

%%

"/*" { BEGIN CMNT; level++; }
<CMNT>"/*" { level++; }
<CMNT>. |
<CMNT>\n ;
<CMNT>"*/" { if (!--level) BEGIN INITIAL; }
{STRING} { printf("String is %s\n", yytext); }
%%
