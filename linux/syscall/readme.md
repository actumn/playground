```bash
$ gcc hello.c
$ strace -o hello.log ./a.out

$ strace -o hello.py.log python3 ./hello.py
```
```bash
$ sar -P ALL 1
$ sar -P ALL 1 1 > sar.log
$ gcc loop.c
$ ./a.out &
$ sar -P ALL 1 1 > sar.loop.log
$ gcc ppidloop.c
$ ./a.out &
$ sar -P ALL 1 1 > sar.ppidloop.log
```
```bash
$ strace -T -o hello-time.log ./a.out
$ strace -tt -o hello-time-micro.log ./a.out
```
