#!/usr/bin/python3

from atds import*

def is_valid(string):
    #sanitize string
    left_parens=0
    right_parens=0
    stack=Stack()
    for i in range(0,len(string)):
        stack.push(string[i])
    while not stack.is_empty():
        char=stack.pop()
        if char=='(':
            left_parens+=1
        elif char==')':
            right_parens+=1
    if left_parens==right_parens:
        return True
    return False