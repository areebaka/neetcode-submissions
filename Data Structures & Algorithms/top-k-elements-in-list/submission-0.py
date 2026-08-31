import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        heap = []
        res = []
        for num in nums:
            if num not in frequencies:
                frequencies[num] = 0
            frequencies[num] += 1
        for num in frequencies:
            if len(heap) < k:
                heapq.heappush(heap, (frequencies[num],num))
            elif len(heap) == k and heap[0][0] < frequencies[num]:
                heapq.heapreplace(heap, (frequencies[num],num))
        while heap:
            frequency, num = heapq.heappop(heap)
            res.append(num)
        return res;