

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

# 首先输入一个2000以内的任意正偶数 #
while True:
    i=int(input('Please enter a number'  ))
    if i>=4 and i<=2000 and i%2==0:
        break
    else:
        print('Please enter a right number')
        
# 输出偶数等于2个质数和的表达式 #        
for a in range(2,1999):
    for b in range(2,1999):
        if a+b == i and isprime(a) and isprime(b):
            print(a, '+', b, '=', i)
