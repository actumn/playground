```shellscript
$ flex calAst.l
$ bison -d calAst.y
$ gcc calAst.tab.c -ly -lfl
```
