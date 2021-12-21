class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ': # 빈 칸 제거
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for value in tokenList:
        if value == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        elif value == '(':
            opStack.push('(')
        elif type(value) == int :
            postfixList.append(value)
        elif not opStack.size() or prec[opStack.peek()] < prec[value]:
            opStack.push(value)
        else:
            while opStack.data and prec[opStack.peek()] >= prec[value]:
                postfixList.append(opStack.pop())
            opStack.push(value)
    while opStack.data:
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    St = ArrayStack()
    for value in tokenList:
        if type(value) == int:
            St.push(value)
        elif value == '+':
            val = St.pop() + St.pop()
            St.push(val)
        elif value == '-':
            val = -St.pop() + St.pop()
            St.push(val)
        elif value == '*':
            val = St.pop() * St.pop()
            St.push(val)
        else:
            val = (1 / St.pop()) * St.pop()
            St.push(val)
    return St.peek()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val