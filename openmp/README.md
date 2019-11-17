For compile openmp test
```shellscript
$ g++ -fopenmp test.cpp
```

For working with large memory
```shellscript
$ g++ -fopenmp column_memory_access.cpp
$ ulimit -s unlimited
$ ./a.out
```
