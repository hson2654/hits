#### privi Esca
OS vuln
i686-w64-mingw32-gcc 40564.c -o MS11-046.exe -lws2_32


```
                   32-bit Target (i686)	          64-bit Target (x86_64)
Compiler Tool	    i686-w64-mingw32-gcc	         x86_64-w64-mingw32-gcc
```
`mingw32 , adding win header to gcc, when compiler x.c file on linux, use  xxx-w64-mingw32-gcc instead of gcc`

```
#include <winsock2.h> (Header file): Tells the compiler the names and signatures of the networking functions so your source code can compile into object code (.o).

    -lws2_32 (Linker flag): Tells the linker to link your program against Winsock2 (ws2_32.dll / libws2_32.a), which contains the actual machine code implementation for those functions.

Without -lws2_32, the linker knows these functions exist, but it doesn't know where to find the actual code to execute them.
```
