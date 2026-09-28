class Solution:
    def maxDepth(self, s: str) -> int:
        left=0
        right=0
        ans=0
        for i in s:
            if i=="(":
                left+=1
            elif i==")":
                right+=1
            a=left-right
            ans=max(ans,a)
        return ans 
        