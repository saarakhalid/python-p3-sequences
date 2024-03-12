#!/usr/bin/env python3

def print_fibonacci(length):
    my_list = []
    i, j = 0, 1

    for _ in range(length):
        my_list.append(i)
        i, j = j, i + j

    print(my_list) 


print_fibonacci(0) 
print_fibonacci(1) 