class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ops = {'+','-','*','/'}
        stack = []
        for t in tokens:
            if t in ops:
                a = int(stack.pop())
                b = int(stack.pop())

                if t == "+":
                    stack.append(b + a)
                elif t == "-":
                    stack.append(b - a)
                elif t == "*":
                    stack.append(b * a)
                else:
                    if (b > 0) == (a > 0):
                        stack.append(b // a)
                    else:
                        stack.append(abs(b) // abs(a) * -1)
            else:
                stack.append(t)
        return int(stack[0])
