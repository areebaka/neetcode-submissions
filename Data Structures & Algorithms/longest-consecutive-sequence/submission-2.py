class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestPatternLen = 0
        sett = set(nums)


        for num in sett:
           if (num - 1) not in sett:
                currLength = 1
                while (num + currLength) in sett:
                    currLength +=1
                longestPatternLen=                  max(currLength,longestPatternLen)   

        return longestPatternLen           
            

