class Solution:
    def isValid(self, s: str) -> bool:

        val = {"}" : "{", "]" : "[", ")" : "("}
        stack = []

        for c in s:

            if(stack and c in val):

                if(stack[-1] != val[c]):
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        
        if(not stack):
            return True
        
        return False
        
        
    