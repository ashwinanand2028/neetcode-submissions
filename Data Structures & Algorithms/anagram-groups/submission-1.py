class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            val = [0]*26
            for c in s:
                
                 val[ord(c) - ord("a")]+=1
                
            res[tuple(val)].append(s)

        return list(res.values())
                