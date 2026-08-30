class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            frequencyCount = [0] * 26
            for c in string:
                frequencyCount[ord(c) - ord('a')] += 1
 # hashmaps can't have lists as key so we're using tuples as a  tuple is basically like a list that can't be changed
            res[tuple(frequencyCount)].append(string)
        return list(res.values())



