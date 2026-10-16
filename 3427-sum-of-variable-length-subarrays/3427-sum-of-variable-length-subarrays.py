class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        for i in range(n):
            subarr=nums[max(0,i-nums[i]):i+1]
            c+=sum(subarr)
        return c
        