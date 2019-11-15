%{
#include <stdio.h>
%}
%token DING DONG DELL
%%
rhyme : sound place { printf("Great!\n"); }
;

sound : DING DONG
;

place : DELL
;
%%
