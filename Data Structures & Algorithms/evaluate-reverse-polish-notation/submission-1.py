class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        


        stack = []



        for c in tokens:

            if c in "+-*/":

                b = int(stack.pop())
                a = int(stack.pop())

                if(c == "+"):
                    stack.append(a + b)
                
                elif(c == "-"):
                    stack.append(a - b)
                
                elif(c == "*"):
                    stack.append((a) * (b))
                
                else:
                    stack.append(int(a/b))
            else:
                stack.append(c)
        return int(stack[0])

