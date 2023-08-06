#!/usr/bin/python3

import time

def factor(n):
    a = (int)(n / 2)
    for i in range(2, a + 1):
        if n % i ==  0:
            p = i
            q = n // p
            print("{:d}={:d}*{:d}".format(n, p, q))
            return
    return
