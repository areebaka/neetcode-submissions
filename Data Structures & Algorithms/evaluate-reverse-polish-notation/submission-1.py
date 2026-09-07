class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
            res=[]
            for s in tokens:
                if s =="+":
                    res.append(res.pop() + res.pop())
                elif s == "-":
                    a, b = res.pop(), res.pop()
                    res.append(b - a)
                elif s == "*":
                    res.append(res.pop() * res.pop())
                elif s == "/":
                    a, b = res.pop(), res.pop()
                    res.append(int(b / a))
                else:
                    res.append(int(s))
            return res[0]