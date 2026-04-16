class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        validPairs = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in validPairs:
                if stack and stack[-1] == validPairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if stack:
            return False
        
        return True
        


