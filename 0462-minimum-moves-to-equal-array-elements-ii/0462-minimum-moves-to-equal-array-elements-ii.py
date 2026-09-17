class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n=len(nums)
        median=nums[n//2]
        c=0
        for i in nums:
            c+=abs(median-i)
        return c
                

        