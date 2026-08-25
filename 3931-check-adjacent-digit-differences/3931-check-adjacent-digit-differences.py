class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        l=[]
        for i in range(1,len(s)):
            a=abs(int(s[i])-int(s[i-1]))
            l.append(a)
        if max(l)>2:
            return False
        else:
            return True