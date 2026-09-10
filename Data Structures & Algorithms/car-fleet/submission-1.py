class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        carTuples = []
        for pos, sp in zip(position, speed):
            carTuples.append((pos, sp))
        carTuples.sort(reverse=True)

        res = []

        for pos, sp in carTuples:
            res.append((target - pos) / sp)

            if len(res) >= 2 and res[-1] <= res[-2]:
                res.pop()

        return len(res)