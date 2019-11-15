
#include "myAst.h"

myAstNode * root;

myAstNode * makeOperTree(myAstNode * left, int op, myAstNode * right) {
	myAstNode * tmp;
	tmp = (myAstNode*)malloc(sizeof(myAstNode));
	tmp->op = op;
	tmp->left = left;		tmp->right = right;
	return tmp;
}

myAstNode * makeNode(int value) {
	myAstNode * tmp;
	tmp = (myAstNode*)malloc(sizeof(myAstNode));
	tmp->op = -1;
	tmp->value = value;
	tmp->left = NULL; 		tmp->right = NULL;
	return tmp;
}

myAstNode * addNonTerminal(int op, myAstNode * left) {
	myAstNode * tmp;
	tmp = (myAstNode*)malloc(sizeof(myAstNode));
	tmp->op = op;	tmp->left = left;	tmp->right = NULL;
	return tmp;
}
void printTree(myAstNode * node, int depth) {
	int i;
	if(node == NULL ) return;
	for(i = 0 ; i < depth ; i++) printf(" ");
	switch(node->op) {
	case -1:	printf("%d\n", node->value );	break;
	case 1:	printf("+\n");		break;
	case 2:	printf("-\n");		break;
	case 3:	printf("*\n");		break;
	case 4:	printf("/\n");		break;
	case 9:	printf("-\n");		break;
	case 10:	printf("()\n");		break;
	}
	printTree(node->left, depth+5);	printTree(node->right, depth+5);
}

int calculate(myAstNode * node)
{
	int left, right, ret = 0;
	if(node == NULL ) return 0;
	left = calculate(node->left);
	right = calculate(node->right);
	switch(node->op) {
	case -1:		ret = node->value;		break;
	case 1:		ret = left+right;		break;
	case 2:		ret = left-right;		break;
	case 3:		ret = left*right;		break;
	case 4:		
		if(right != 0) ret = left/right;
		else printf("error : divide by zero\n");
	break;
	case 9:		ret = - left;		break;
	case 10:		ret = left;			break;
	}
	return ret;
}

