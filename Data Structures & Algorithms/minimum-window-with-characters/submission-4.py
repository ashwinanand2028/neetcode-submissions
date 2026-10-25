class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if(not t or len(t) > len(s)):
            return ""
        
        ct = {}
        for c in t:
            ct[c] = ct.get(c, 0) + 1
        
        window = {}
        have = 0 
        need = len(ct)

        res = [0,0]
        res_len = float("inf")

        l = 0 
        for r in range (len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if(s[r] in ct and window[s[r]] == ct[s[r]]):
                have +=1
            
            while (have == need):
                if(r - l + 1 < res_len):
                    res = [l, r]
                    res_len = r - l + 1

                window[s[l]] -=1

                if(s[l] in ct and window[s[l]] < ct[s[l]]): 
                    have -=1
                
                l +=1
        
        if(res_len != float("inf")):
            return s[res[0]: res[1] + 1]
        else:
            return ""
                








