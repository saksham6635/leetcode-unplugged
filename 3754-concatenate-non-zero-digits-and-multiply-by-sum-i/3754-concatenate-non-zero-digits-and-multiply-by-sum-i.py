class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        a=str(n)
        b=a.replace("0","")
        c=int(b)
        d=0
        for i in a:
            d+=int(i)
        return d*c
        