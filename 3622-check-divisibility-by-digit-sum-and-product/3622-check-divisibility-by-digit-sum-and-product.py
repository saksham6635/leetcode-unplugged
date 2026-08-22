class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num=str(n)
        digits=list(num)
        total,product=0,1
        for i in digits:
            total+=int(i)
            product*=int(i)
        return n%(total+product)==0

