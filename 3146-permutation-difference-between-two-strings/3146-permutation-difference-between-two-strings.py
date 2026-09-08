class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        c=0
        for i in range(len(s)):
            if s[i]==t[i]:
                c+=0
            else:
                a=abs(i-t.index(s[i]))
                c+=a
        return c
            
        