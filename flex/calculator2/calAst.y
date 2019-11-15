%{
#include <stdio.h>
#include "myAst.h"

void yyerror(char*);
%}

%union {
	myAstNode * ast;
	int ival;
}

%token <ival> NUMBER
%type <ast> expression 
%left '-' '+'
%left '*' '/'
%nonassoc UMINUS

%%
statement_list	: statement	
		| statement_list '\n' statement  
		;
statement	:  expression
	{
		root = $1;
		printf("-- Print AST --\n");
		printTree(root, 0);
		printf("result=%d\n", calculate(root));
	}
	|
	;
expression
	: expression '+' expression 	{ $$ = makeOperTree($1, 1, $3); }
	| expression '-' expression 	{ $$ = makeOperTree($1, 2, $3); }
	|  expression '*' expression	{ $$ = makeOperTree($1, 3, $3); }
	|  expression '/' expression	{ $$ = makeOperTree($1, 4, $3); }
	|  '-' expression %prec UMINUS	
		{ $$ = makeOperTree($2, 9, NULL); /*addNonTerminal(9, $2);*/ }
	| '(' expression  ')'	{ $$ = $2; }
	|  NUMBER		{ $$ = makeNode($1); }
	;
%%
#include "lex.yy.c"
#include "myAst.c"
void yyerror(char* s) {
	printf("%s\n", s);
}
int main() {
	return yyparse();
}
