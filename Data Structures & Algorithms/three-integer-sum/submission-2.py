class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        ascNums = sorted(nums)

        for i in range(len(ascNums)):
            p1 = i + 1
            p2 = len(ascNums) - 1

            if i > 0 and ascNums[i] == ascNums[i - 1]:
                continue

            while p1 < p2:
                total = ascNums[i] + ascNums[p1] + ascNums[p2]

                if total > 0:
                    p2 -= 1
                elif total < 0:
                    p1 += 1
                else:
                    res.append([ascNums[i], ascNums[p1], ascNums[p2]])
                    p1 += 1
                    p2 -= 1

                    while p1 < p2 and ascNums[p1] == ascNums[p1 - 1]:
                        p1 += 1

                    while p1 < p2 and ascNums[p2] == ascNums[p2 + 1]:
                        p2 -= 1

        return res