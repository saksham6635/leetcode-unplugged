class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        f={}
        a=float("inf")
        l=[]
        for i in str(n):
            f[i]=f.get(i,0)+1
        for i in f:
            a=min(a,f[i])
        for i in f:
            if f[i]==a:
                l.append(int(i))
        return min(l)
        
        