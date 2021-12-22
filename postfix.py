# In this file, we imitate the function 'expression(str)' by the 'Stack', one of data structures.
# import re for regular expression
import re


# Definition of the class 'Stack'
# Actually, What Stack can do is what list can do. there are little differences.
# Property of the first-in-last-out
class Stack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


# 'Extracting the proper str' process to convert an infix form to a postfix form
# We use regular expression of python (re module is used in here.)
def remove_space(expression: str) -> str:
    extract = re.sub(r'\s', '', expression)
    return extract


# Actual process of postfix
def infix_to_postfix(extract: str) -> list:
    # order of operations
    operation_order = {
        '^': 4,
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    op_stack = Stack()
    postfix_list = []

    for i, value in enumerate(extract):
        # case of (,)
        if value == ')':
            while op_stack.peek() != '(':
                postfix_list.append(op_stack.pop())
            op_stack.pop()
        elif value == '(':
            op_stack.push('(')

        # case of numbers
        elif value.isdigit() or value == '.':
            if i == 0 or (not extract[i-1].isdigit() and extract[i-1] != '.'):
                postfix_list.append(value)
            else:
                postfix_list[-1] += value
        # case of operators
        elif op_stack.is_empty() or operation_order[op_stack.peek()] < operation_order[value]:
            op_stack.push(value)
        else:
            while op_stack.data and operation_order[op_stack.peek()] >= operation_order[value]:
                postfix_list.append(op_stack.pop())
            op_stack.push(value)

    # add remaining elements in the stack to list
    while op_stack.data:
        postfix_list.append(op_stack.pop())

    return postfix_list


# Calculation
def postfix_eval(postfix_list) -> int or float:
    st = Stack()
    for value in postfix_list:
        if value == re.sub('[^0-9.]', '', value):
            st.push(value)
        elif value == '+':
            val = float(st.pop()) + float(st.pop())
            st.push(val)
        elif value == '-':
            val = -float(st.pop()) + float(st.pop())
            st.push(val)
        elif value == '*':
            val = float(st.pop()) * float(st.pop())
            st.push(val)
        elif value == '/':
            val = (1 / float(st.pop())) * float(st.pop())
            st.push(val)
        else:
            pos = float(st.pop())
            pre = float(st.pop())
            val = pre ** pos
            st.push(val)
    return st.peek()


# From a string expression, we evaluate a real value, like the 'expression' function already in python
def solution(expression: str) -> int or float:
    if not expression:
        return 'Blank!'
    try:
        tokens = remove_space(expression)
        postfix = infix_to_postfix(tokens)
        val = postfix_eval(postfix)
    except:
        return "You inserted a wrong formula!"

    return val


