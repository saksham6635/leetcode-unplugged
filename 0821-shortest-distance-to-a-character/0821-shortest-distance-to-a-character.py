class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        l = []
        for i in range(n):
            a = float("inf")   
            for j in range(n):
                if s[j] == c:
                    a = min(a, abs(j - i))
            l.append(a)
        return l
