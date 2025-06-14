#!/usr/bin/python3
for i in range(122, 96, -1):
    #Uppercase: odd Ascii, lowercase: even Ascii 
    print("{}".format(chr(i) if i % 2 == 0 else chr(i - 32)), end="")
