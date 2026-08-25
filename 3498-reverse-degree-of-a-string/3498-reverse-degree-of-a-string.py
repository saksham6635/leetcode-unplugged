class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            idx=(123-ord(s[i]))*(i+1)
            ans+=idx
        return ans
