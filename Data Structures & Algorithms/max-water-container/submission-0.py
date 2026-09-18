class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            # area = width * height
            # r - l = width between the lines.
            waterFill =  (r - l) * min(heights[l], heights[r])
            res = max(res, waterFill)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res