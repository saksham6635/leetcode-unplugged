class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        return max(0,n-k,m-k)*k
        