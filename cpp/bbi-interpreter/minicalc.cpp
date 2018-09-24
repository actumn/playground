#include <iostream>
#include <cstdlib>
#include <cctype>
using namespace std;

enum TknKind {		// 토큰의 종류
	Print, Lparen, Rparen, Plus, Minus, Multi, Divi,
	Assign, VarName, IntNum, EofTkn, Others
};

struct Token {
	TknKind kind;	// 토큰의 종류
	int intVal;		// 상숫값이나 변수 번호
	Token() { kind = Others; intVal = 0; }
	Token(TknKind k, int d=0) { kind = k; intVal = d; }
};

void input();
void statement();
void expression();
void term();
void factor();
Token nextTkn();
int nextCh();
void operate(TknKind op);
void push(int n);
int pop();
void chkTkn(TknKind kd);

#define STK_SIZ 20				// 스택 크기
int stack[STK_SIZ + 1];			// 스택
int stkct;						// 스택 관리
Token token;					// 토큰 저장
char buf[80], *bufp;			// 입력용
int ch;							// 가져온 문자를 저장
int var[26];					// 변수 a-z
int errF;						// 오류 발생

int main() {
	while (1) {
		input();
		token = nextTkn();					// 최초 토큰
		if (token.kind == EofTkn) exit(1);	// 종료
		statement();						// 문 실행
		if (errF) cout << " --err--: " << errF << endl;
	}

	return 0;
}



void input()
{
	errF = 0; stkct = 0;	// 초기 설정
	cin.getline(buf, 80);	// 80문자 이내의 입력
	bufp = buf;				// 시작 문자 위치
	ch = nextCh();			// 초기 문자 가져오기
}

// 문
void statement()
{
	int vNbr;

	switch (token.kind) {
	case VarName:				// 대입문
		vNbr = token.intVal;	// 대입할 곳 보존
		token = nextTkn();
		chkTkn(Assign); if (errF) break;	// '=' 일 것
		token = nextTkn();
		expression();						// 우변 계산
		var[vNbr] = pop();					// 대입 실행
		return;
	case Print:					// Print 문: '?'
		token = nextTkn();
		expression();
		chkTkn(EofTkn);	if (errF) break;
		cout << " " << pop() << endl;
		return;
	default:
		errF = 1;
	}

	chkTkn(EofTkn);				// 행 끝 검사
}



// 식
void expression()
{
	TknKind op;

	term();
	while(token.kind == Plus || token.kind == Minus) {
		op = token.kind;
		token = nextTkn(); term(); operate(op);
	}
}

// 항
void term()
{
	TknKind op;
	factor();
	while(token.kind == Multi || token.kind == Divi) {
		op = token.kind;
		token = nextTkn(); factor(); operate(op);
	}
}

// 인자
void factor()
{
	switch (token.kind) {
	case VarName:			// 변수
		push(var[token.intVal]);
		break;
	case IntNum:			// 정수 상수
		push(token.intVal);
		break;
	case Lparen:			// '( )'
		token = nextTkn();
		expression();
		chkTkn(Rparen);		// ')' 일 것
		break;
	default:
		errF = 10;
	}
	token = nextTkn();
}

// 다음 토큰
Token nextTkn()
{
	TknKind kd = Others;
	int num;

	while (isspace(ch)) 		// 공백 건너뛰기
		ch = nextCh();

	if (isdigit(ch)) {
		for (num = 0; isdigit(ch); ch = nextCh())
			num = num * 10 + (ch - '0');

		return Token(IntNum, num);
	}
	else if (islower(ch)) {		// 변수
		num = ch - 'a';			// 변수 번호 0-25
		ch = nextCh();
		return Token(VarName, num);
	}
	else {
		switch (ch) {
		case '(': kd = Lparen; break;
		case ')': kd = Rparen; break;
		case '+': kd = Plus; break;
		case '-': kd = Minus; break;
		case '*': kd = Multi; break;
		case '/': kd = Divi; break;
		case '=': kd = Assign; break;
		case '?': kd = Print; break;
		case '\0': kd = EofTkn; break;
		}
		ch = nextCh();
		return Token(kd);
	}
}

int nextCh()
{
	if (*bufp == '\0') return '\0'; else return *bufp++;
}

void operate(TknKind op)
{
	int d2 = pop(), d1 = pop();

	if (op == Divi && d2 == 0) { cout << " division by 0\n "; errF = 100; }
	if (errF) return;
	switch (op) {
	case Plus:	push(d1+d2); break;
	case Minus:	push(d1-d2); break;
	case Multi:	push(d1*d2); break;
	case Divi:	push(d1/d2); break;
	}
}

void push(int n)
{
	if (errF) return;
	if (stkct+1 > STK_SIZ) { cout << "stack overflow\n"; exit(1); }
	stack[++stkct] = n;
}

int pop()
{
	if (errF) return 1;
	if (stkct < 1) { cout << "stack underflow\n"; exit(1); }
	return stack[stkct--];
}

// 토큰 종류 확인
void chkTkn(TknKind kd)
{
	if (token.kind != kd) errF = 1000;
}

