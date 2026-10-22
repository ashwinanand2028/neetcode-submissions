class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #sliding window type of problem i think

        count = {}
        l = 0 
        mLen = 0 
        mFreq = 0 

        for r in range (len(s)):

            count[s[r]] = count.get(s[r], 0) + 1
            mFreq = max(mFreq, count[s[r]])

            if(r - l + 1 - mFreq > k):
                count[s[l]] -=1
                l+=1
            
            mLen = max(mLen, r - l + 1)
            
            
            
        
        return mLen


    
            
        
            

            







            
        