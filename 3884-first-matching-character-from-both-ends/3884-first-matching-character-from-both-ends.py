class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n=len(s)
        l=[]
        for i in range(len(s)):
            if s[i]==s[n-i-1]:
                l.append(i)
        if len(l)>=1:
            return min(l)
        else:
            return -1
    
        