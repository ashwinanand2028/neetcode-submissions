class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        

        t = s.lower()

        newt = ""
        for i in range(len(t)):
            if(t[i].isalnum()): 
                newt = newt + t[i]


        r = ""
        
        for i in range(len(t)-1, -1, -1):
            if(t[i].isalnum()): 
                r = r + t[i]
        
        return(newt == r)



            

            