class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = ["+", "-", "*", "/"]

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            
            if t in operators:
                val2, val1 = stack.pop(), stack.pop()

                if t == "+":
                    stack.append(val1 + val2)
                elif t == "-":
                    stack.append(val1 - val2)
                elif t == "*":
                    stack.append(val1 * val2)
                elif t == "/":
                    stack.append(int(val1 / val2))
        

        return stack.pop()