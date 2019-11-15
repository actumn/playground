```shellscript
$ bison -d ding.y
$ flex ding.l
$ gcc ding.tab.c lex.yy.c -ll -ly
$ ./a.out
ding

dong

dell
Great!
```
