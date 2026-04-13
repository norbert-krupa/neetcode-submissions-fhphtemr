class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            
            if c == ")" or c == "}" or c == "]":
                if stack == []:
                    return False
                
                last = stack.pop()

                if c == ")" and last != "(":
                    return False
                elif c == "}" and last != "{":
                    return False
                elif c == "]" and last != "[":
                    return False
        
        if stack != []:
            return False
        
        return True

