class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l < r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            
            if s[l].lower()!=s[r].lower():
                skipL = s[l+1:r+1]
                skipR = s[l:r]
                return skipL==skipL[::-1] or skipR==skipR[::-1]

            l+=1
            r-=1
        return True