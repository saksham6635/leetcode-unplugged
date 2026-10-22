class Solution:
    def findLHS(self, nums: list[int]) -> int:
        ans=0
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1
        for num in f:
            if num+1 in f:
                ans=max(ans,f[num]+f[num+1])
        return ans 
        
        
            
