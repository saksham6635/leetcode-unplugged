class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1
        ans=0
        for i in f:
            if f[i]==1:
                ans+=i
        return ans 
        