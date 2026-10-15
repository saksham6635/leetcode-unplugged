class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        l=[]
        for i in range(n):
            for j in range(i,n):
                subarr=nums[i:j+1]
                l.append(subarr)
        for i in l:
            a=len(set(i))
            ans+=a**2
        return ans 

        