class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        f={}
        l=[]
        for i in str(n):
            f[i]=f.get(i,0)+1
        min_freq=min(f.values())
        for i in f:
            if f[i]==min_freq:
                l.append(int(i))
        return min(l)
        
        