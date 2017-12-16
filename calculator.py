#!/usr/bin/env python3
import sys
if len(sys.argv) != 2:
    print("Parameter Error")
try:
    a = sys.argv[1]
    e = int(a)
except:
    print("Parameter Error")
finally:
    b = e-3500
    if b<=1500:
        c=b*0.03
    elif b<=4500:
        c=b*0.1-105
    elif b<=9000:
        c=b*0.2-555
    elif b<=35000:
        c=b*0.25-1005
    elif b<=55000:
        c=b*0.3-2755
    elif b<=80000:
        c=b*0.35-5505
    else:
        c=b*0.45-13505
    d = format(c,".2f")
    print(d)

