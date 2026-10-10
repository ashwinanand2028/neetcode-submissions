class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      ns = [0]*26

      nt = [0]*26


      for i in range(len(s)):
        ns[ord(s[i]) - ord("a")]+=1
      
      for i in range(len(t)):
        nt[ord(t[i]) - ord("a")]+=1
      
      for i in range(len(ns)):
        if(ns[i] != nt[i]):
          return False
        

      return True

      
      

        
        