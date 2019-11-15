#ifndef __MYAST_H__
#define __MYAST_H__
#include <stdio.h>
#include <stdlib.h>

typedef struct _myAst {
	int op;	// 연산자 종류에 따라 +: 1, -: 2, *: 3, /: 4, 음수:9
	int value;	// 터미널의 경우 op = -1
	struct _myAst * left;	// 터미널의 경우 NULL
	struct _myAst * right;
} myAstNode;

myAstNode * makeOperTree(myAstNode * left, int op, myAstNode * right);
myAstNode * makeNode(int value);
// myAstNode * addNonTerminal(int op, myAstNode * left);
void printTree(myAstNode * node, int depth);
int calculate(myAstNode * node);

extern myAstNode * root;
#endif
