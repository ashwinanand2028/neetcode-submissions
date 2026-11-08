class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        res = [0] * len(temperatures)
        stack = [] # (index, temp)

        for i, t in enumerate(temperatures):

            while(stack and t > stack[-1][1]):

                istack , tstack = stack.pop()
                res[istack]  = i - istack
            stack.append((i, t))
        
        return res