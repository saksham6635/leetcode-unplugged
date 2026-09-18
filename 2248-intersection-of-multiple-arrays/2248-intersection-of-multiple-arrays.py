class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        result=set(nums[0])
        for i in nums[1:]:
            result&=set(i)
        return sorted(result)

        