class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s == 0:
            return 0 if n >= 1 else -1
        ans = -1
        for i in range(10**n - 1, -1, -1): 
            if sum(map(int, str(i))) == s:
                ans = i
                break
        return ans
