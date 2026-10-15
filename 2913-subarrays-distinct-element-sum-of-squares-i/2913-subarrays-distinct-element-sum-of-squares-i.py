class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            for j in range(i,n):
                subarr=nums[i:j+1]
                distinct=len(set(subarr))
                ans+=(distinct)**2
        return ans 

        