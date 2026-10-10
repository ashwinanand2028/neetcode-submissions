class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      
      res = defaultdict(int)
      
      for i in range(len(s)):
        res[s[i]] +=1
        res[t[i]] -=1
      
      for i in res.values():
        if i!= 0:
            return False
      return True

        
        