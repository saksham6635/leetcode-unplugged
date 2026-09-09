class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        elif n in range(1000,10**6):
            return n-10**3 +1
        elif n in range(10**6,10**9):
            return 2*(n-10**6 +1)+(10**6-10**3)
        elif n in range(10**9,10**12):
            return 3*(n-10**9+1)+ 2*(10**9-10**6)+(10**6-10**3)
        elif n in range(10**12,10**15):
            return 4*(n - 10**12 +1)+3*(10**12 - 10**9)+2*(10**9 - 10**6)+(10**6 - 10**3)
        else:
            return 5*(n-10**15+1)+4*(10**15-10**12)+3*(10**12 - 10**9)+2*(10**9 - 10**6)+(10**6 - 10**3)
