class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        sum = 0
        for token in tokens:
            if stack and (token == "+" or token == "-" or token == "*" or token == "/"):
                second = int(stack.pop())
                first = int(stack.pop())
                if token == "+":
                    stack.append(second + first)
                if token == "-":
                    stack.append(first - second)
                if token == "*":
                    stack.append(first * second)
                if token == "/":
                    stack.append(math.trunc(first / second))
            else:
                stack.append(int(token))
        return stack.pop()