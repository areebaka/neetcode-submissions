class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString= ''
        for c in s:
            if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
                cleanString += c.lower()
        return cleanString == cleanString[::-1]    
   
    