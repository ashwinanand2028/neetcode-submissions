class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1

        lMax = height[l]
        rMax = height[r]

        ans = 0

        if(len(height) == 0):
            return 0

        
        while(l < r):

            if(lMax < rMax):
                l +=1
                lMax = max(lMax, height[l])
                ans += lMax - height[l]
            
            else:
                r -=1
                rMax = max(rMax, height[r])
                ans += rMax - height[r]
        
        return ans




