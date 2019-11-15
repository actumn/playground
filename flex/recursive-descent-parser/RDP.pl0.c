#include <stdio.h>

enum yytokentype {
    TCONST = 258,
    TVAR = 259,
    TPROC = 260,
    TCALL = 261,
    TBEGIN = 262,
    TIF = 263,
    TTHEN = 264,
    TWHILE = 265,
    TDO = 266,
    TEND = 267,
    ID = 268,
    NUM = 269,
    ODD = 270,
    NE = 271,
    LE = 272,
    GE = 273,
    ASSIGN = 274
};

int yylval;
int yytoken=0;
int ln=1, cp=0;

int yylex();
void Block();
void Statement();
void Condition();
void Exp();
void Term();
void Factor();
void yyerror();

int gettoken() {
	yytoken=yylex();
}

int match(int ch) {
	if (yytoken==ch) { 
        gettoken(); 
        return 1; 
    }
	return 0;
}

int Program() {
	gettoken();
	Block(); 
	if (match('.')) return 1; else return 0;
}

void Block() {
	if (match(TCONST)) {
        do {
            match(ID);
            match(ASSIGN);
            match(NUM);
        } while (match(','));
        match(';');
    }
	if (match(TVAR)) {
        do {
            match(ID);
        } while (match(','));
        match(';');
    }
	while (match(TPROC))  {
        match(ID);
        match(';');
        Block();
        match(';');
    }
	Statement();
}

void Statement() {
	if (match(ID)) {
        if (!match(ASSIGN)) yyerror("assign st error\n");
        Exp(); 
    }
	else if (match(TCALL)) {
        if (!match(ID)) yyerror("call procedure error\n");
    }
	else if (match(TBEGIN)) {
        do {
            Statement();
        } while (match(';'));

        match(TEND);
    }
	else if (match(TWHILE)) {
        Condition();
        match(TDO);
        Statement();
    }
	else if (match(TIF)) {
        Condition();
        match(TTHEN);
        Statement();
    }
	return;
}
void Condition() {
	if (match(ODD)) Exp();
	else {	
		Exp(); 
		if (match('=') || match('<') || match('>') || match(NE) || match(GE) || match(LE))	Exp();
		else yyerror("condition error\n");
	}
}

void Exp() { 
	Term(); 
	while ( match('+') || match('-') ) Term();	
}

void Term() {  
	Factor(); 
	while ( match('*') || match('/') ) Factor();
}

void Factor() {  
	if ( match(ID) || match(NUM) ) return;
	if ( match('(')) {	
		Exp(); 
		if (match(')')) return;
	}
	yyerror("factor error");
}


