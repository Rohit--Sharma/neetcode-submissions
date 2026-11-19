class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(a, b):
            return a + b
        def subtract(a, b):
            return a - b
        def multiply(a, b):
            return a * b
        def divide(a, b):
            return int(a / b) # Just a // b doesn't work here for negatives because we want to truncate towards zero.

        operators = {'+': add, '-': subtract, '*': multiply, '/': divide}

        stack = []
        for t in tokens:
            if t in operators:
                right = stack.pop()
                left = stack.pop()
                stack.append(operators[t](left, right))
            else:
                stack.append(int(t))

        return stack[-1]
