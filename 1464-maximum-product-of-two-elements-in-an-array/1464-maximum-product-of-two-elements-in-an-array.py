class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum=max(nums)
        idx=nums.index(maximum)
        nums.pop(idx)
        c=0
        for i in range(len(nums)):
            c=max(c,(nums[i]-1)*(maximum-1))
        return c




        