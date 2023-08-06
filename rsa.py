#!/usr/bin/python3

import time
import sys 

def factor(n):
    if n == 1:
        return "1=1*1"
    a = n // 2
    for i in range(2, a + 1): 
        if n % i ==  0:  
            p = i 
            q = n // p
            print("{:d}={:d}*{:d}".format(n, q, p)) 
            return
    return ("{:d}={:d}*1".format(n, n)) 

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
except IOError:
    sys.exit(1)


for line in lines:
    n = int(line.strip())
    factorisation = factor(n)
