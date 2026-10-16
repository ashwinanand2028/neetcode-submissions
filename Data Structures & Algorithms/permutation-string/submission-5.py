class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n = len(s1)

        check = [0] * 26
        cur = [0] * 26

        if(n > len(s2)):
            return False
        
        for c in s1:
            check[ord(c) - ord("a")] +=1

        for r in range (len(s2)):
            if(r >= n):
                cur[ord(s2[r - n]) - ord("a")] -=1
            cur[ord(s2[r]) - ord("a")] +=1
            if(cur == check):
                return True
        return False


            


            






        