class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            t=""
            for i in range(1,len(s)):
                a=(int(s[i])+int(s[i-1]))%10
                t+=str(a)
            s=t
        return len(set(t))==1