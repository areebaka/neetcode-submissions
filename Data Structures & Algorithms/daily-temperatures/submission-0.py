class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            res = [0] * len(temperatures)
            stack = []  # pair: [temp, index]
        
            for i in range(len(temperatures)):
                current = temperatures[i]
                while stack:
                    old_temp = stack[-1][0]
                    if current <= old_temp:
                        break
                    old_temp, old_index = stack.pop()
                    res[old_index] = i - old_index

                stack.append((current, i))
            return res