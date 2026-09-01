class Solution:

    def encode(self, strs: List[str]) -> str:
        newStrs = []
        for string in strs:
            count = len(string)
            newStrs.append(str(count) + "S"  + string)
        return "".join(newStrs);

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0
        while i < len(s):
            while s[j] != 'S':
                j += 1
            length = int(s[i:j]) # int b/w i&j #doesnt include j 
            i=j+1
            j=length+i
            res.append(s[i:j])
            i = j
        
        return res
        

            
                
            
            
