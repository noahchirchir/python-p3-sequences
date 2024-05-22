#!/usr/bin/env python3

def print_fibonacci(length):
    fib_seq=[]
    if int(length) == 0 :
        print(fib_seq)
    elif int(length) == 1:
        fib_seq.append(0)
        print(fib_seq)   
    elif int(length)==2 :
        fib_seq.append(0)
        fib_seq.append(1)
        print(fib_seq)
    
    else :

        prev=0
        next=1
        fib_seq.append(prev)
        fib_seq.append(next)
        while len(fib_seq) < int(length):
            temp=next
            next= prev+next
            prev=temp
            fib_seq.append(next)
        
        print(fib_seq)
    