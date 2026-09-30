class Solution:
    def findValidPair(self, s: str) -> str:
        f={}
        t=""
        for i in s:
            f[i]=f.get(i,0)+1
        for i in range(len(s)-1):
            a,b=s[i],s[i+1]
            if a!=b and f[a]==int(a) and f[b]==int(b):
                return a+b
        return ""
        