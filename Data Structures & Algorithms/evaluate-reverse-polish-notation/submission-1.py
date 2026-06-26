from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stack = deque()
        for i in range(len(tokens)):
            t = tokens[i]

            if t in ops:
                if t == "+":
                    a1, a2 = stack.pop(), stack.pop()
                    stack.append(a1 + a2)
                elif t == "-":
                    a1, a2 = stack.pop(), stack.pop()
                    stack.append(a2 - a1)
                elif t == "*":
                    a1, a2 = stack.pop(), stack.pop()
                    stack.append(a1 * a2)
                elif t == "/":
                    a1, a2 = stack.pop(), stack.pop()
                    res = a2/a1
                    if res < 0:
                        stack.append(math.ceil(res))
                    else:
                        stack.append(math.floor(res))

            else:
                stack.append(int(t))
        
        return stack.pop()