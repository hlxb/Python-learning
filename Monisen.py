# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-

# 定义一个判断质数（素数）的函数 #
def isprime(x):
    if x == 1:
        return False
    else:
        for i in range(2,x):
            if x%i == 0:
                return False
        return True

def get_monisen(n):
    count = 0
    P = 2
    while True:
        if isprime(P) and isprime(2**P-1):
            count += 1
            if count == n:
                break
        P += 1
    return 2**P-1

print(get_monisen(6))
                
    
        
        
