%{
#include <stdio.h>

void yyerror(char*);

typedef struct {
    int tag;
    union {
        float fval;
        int ival;
    };
} vtype;

vtype vbltable[26];

%}

%union {
	vtype dval;
	int ival;
}
%token <dval> NUMBER
%token <ival> NAME
%type <dval> expression
%left '-' '+'
%left '*' '/' 
%nonassoc UMINUS

%%
Goal		: statement_list
statement_list	: statement	
		| statement_list '\n' statement  
		;
statement	: expression {
    if ($1.tag) {
        printf("%lf\n", $1.fval);
    }
    else {
        printf("%d\n", $1.ival);
    }
}
| NAME '=' expression { 
    vbltable[$1] = $3; 
    if ($3.tag) {
        printf("%lf\n", $3.fval);
    }
    else {
        printf("%d\n", $3.ival);
    }
}
;
expression	: expression '+' expression {
    if ($1.tag && $3.tag) {
        $$.tag = 1;
        $$.fval = $1.fval + $3.fval; 
    } else if (!$1.tag && !$3.tag) {
        $$.tag = 0;
        $$.ival = $1.ival + $3.ival;
    } else if ($1.tag && !$3.tag) {
        $$.tag = 1;
        $$.fval = $1.fval + $3.ival; 
    } else if (!$1.tag && $3.tag) {
        $$.tag = 1;
        $$.fval = $1.ival + $3.fval;
    }
}
| expression '-' expression { 
    if ($1.tag && $3.tag) {
        $$.tag = 1;
        $$.fval = $1.fval - $3.fval; 
    } else if (!$1.tag && !$3.tag) {
        $$.tag = 0;
        $$.ival = $1.ival - $3.ival;
    } else if ($1.tag && !$3.tag) {
        $$.tag = 1;
        $$.fval = $1.fval - $3.ival; 
    } else if (!$1.tag && $3.tag) {
        $$.tag = 1;
        $$.fval = $1.ival - $3.fval;
    }
}
| expression '*' expression { 
    if ($1.tag && $3.tag) {
        $$.tag = 1;
        $$.fval = $1.fval * $3.fval; 
    } else if (!$1.tag && !$3.tag) {
        $$.tag = 0;
        $$.ival = $1.ival * $3.ival;
    } else if ($1.tag && !$3.tag) {
        $$.tag = 1;
        $$.fval = $1.fval * $3.ival; 
    } else if (!$1.tag && $3.tag) {
        $$.tag = 1;
        $$.fval = $1.ival * $3.fval;
    }
}
| expression '/' expression { 
    if( $3.tag && $3.fval == 0 || !$3.tag && $3.ival == 0 ) 
        yyerror("divide by zero");
    else {
        if ($1.tag && $3.tag) {
            $$.tag = 1;
            $$.fval = $1.fval / $3.fval; 
        } else if (!$1.tag && !$3.tag) {
            $$.tag = 0;
            $$.ival = $1.ival / $3.ival;
        } else if ($1.tag && !$3.tag) {
            $$.tag = 1;
            $$.fval = $1.fval / $3.ival; 
        } else if (!$1.tag && $3.tag) {
            $$.tag = 1;
            $$.fval = $1.ival / $3.fval;
        }
    } 
}
|  '-' expression %prec UMINUS { 
    if ($2.tag) {
        $$.tag = 1;
        $$.fval = -$2.fval;
    }
    else {
        $$.tag = 0;
        $$.ival = -$2.ival;
    }
}
| '(' expression ')' { $$ = $2; }
|  NUMBER { 
    if ($1.tag) {
        $$.tag = 1;
        $$.fval = $1.fval;
    }
    else {
        $$.tag = 0;
        $$.ival = $1.ival;
    }
}
|  NAME { $$ = vbltable[$1]; }   
;
%%

#include "lex.yy.c"
void yyerror(char* s) {
	printf("error: %s\n", s);
}
int main() {
	return yyparse();
}
