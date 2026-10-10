class Solution:
    def isPalindrome(self, s: str) -> bool:

        t = s.lower()

        newt = ""

        for i in range(len(t)):
            if t[i].isalnum():
                newt = newt + t[i]

        reverset =""
        
        for i in range(len(t)-1, -1, -1):
            if t[i].isalnum():
                reverset = reverset + t[i]

        return (reverset == newt)



            

            