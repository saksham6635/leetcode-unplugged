class Solution:
    def mirrorDistance(self, n: int) -> int:
        s=""
        c=n
        while n>0:
            a=n%10
            n=n//10
            s+=str(a)
        return abs(c-int(s))
    
        