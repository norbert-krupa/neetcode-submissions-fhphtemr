class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        corr = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in corr:
                if stack and stack[-1] == corr[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False
        
        return True

