class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        elif n in range(1000,100001):
            return n-1000+1
        
        