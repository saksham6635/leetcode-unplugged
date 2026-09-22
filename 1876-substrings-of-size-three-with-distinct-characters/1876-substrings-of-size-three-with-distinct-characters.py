class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c=0
        n=len(s)
        for i in range(n-3+1):
            a=s[i:i+3]
            if len(a)==len(set(a)):
                c+=1
        return c
        