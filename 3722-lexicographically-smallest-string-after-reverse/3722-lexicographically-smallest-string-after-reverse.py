class Solution:
    def lexSmallest(self, s: str) -> str:
        l,m=[],[]
        n=len(s)
        for i in range(1,n+1):
            l.append(s[:i][::-1]+s[i:])
        a=min(l)
        for i in range(n):
            m.append(s[:i]+s[i:][::-1])
        b=min(m)
        return min(a,b)
       
        
        