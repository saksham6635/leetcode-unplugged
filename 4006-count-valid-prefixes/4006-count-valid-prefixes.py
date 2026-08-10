class Solution:
    def countValidPrefixes(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(n):
            sub=s[:i+1]
            if len(sub)==1:
                ans+=1
            elif sub=="10" or sub=="01":
                ans+=1
            elif abs(sub.count("1")-sub.count("0"))<=1:
                ans+=1
        return ans 

        