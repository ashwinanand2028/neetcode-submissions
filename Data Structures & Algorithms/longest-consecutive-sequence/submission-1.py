class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        val = defaultdict(int)

        res = 0

        for num in set(nums):

            val[num] = val[num-1]+val[num+1]+1

            val[num-val[num-1]] = val[num]
            val[num+val[num+1]] = val[num]

            res = max(res, val[num])
        
        return res

            