import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        heap = []
        res = []
        for num in nums:
            frequencies[num] = 1 + frequencies.get(num,0)
        for num in frequencies:
            heapq.heappush(heap, (frequencies[num], num)) 
            if len(heap) > k: 
                heapq.heappop(heap) 

        while heap:
            frequency, num = heapq.heappop(heap)
            res.append(num)
        return res;