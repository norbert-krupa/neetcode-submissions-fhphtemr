class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = ["+", "-", "*", "/"]

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            
            if t in operators:
                opp2, opp1 = stack.pop(), stack.pop()

                if t == "+":
                    stack.append(opp1 + opp2)
                elif t == "-":
                    stack.append(opp1 - opp2)
                elif t == "*":
                    stack.append(opp1 * opp2)
                elif t == "/":
                    stack.append(int(opp1 / opp2))
        
        return stack.pop()