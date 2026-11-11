class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        l = 0 
        r = len(nums) 

        while(l < r):

            val = (l + (r- 1)) // 2

            if(nums[val] == target):
                return val
            elif(nums[val] > target):
                r = val 
            else:
                l = val + 1
        
        return -1

