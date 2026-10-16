class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        n = len(s1)

        for l in range(len(s2) - n + 1):
            if sorted(s2[l:l + n]) == s1:
                return True

        return False


            






        