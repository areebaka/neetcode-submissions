class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString= ''
        reversedString=''
        for c in s:
            if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
                cleanString += c.lower()
    
        for c in cleanString:
            reversedString = c + reversedString  
    
        return cleanString == reversedString