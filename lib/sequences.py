#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = []
    if length > 0:
        '''prints 0 when length = 1'''
        fibonacci.append(0)
    if length > 1:
        '''prints 0\\n1 when length = 2'''
        fibonacci.append(1)
    if length > 2:
        '''prints 0\\n1\\n1\\n2\\n3\\n5\\n8\\n13\\n21\\n34 when length = 10'''
        for i in range(2, length):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])


    print(fibonacci)


    