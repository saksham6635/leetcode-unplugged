class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ans =0
        if len(nums)==len(set(nums)):
            return 0
        for i in set(nums):
            if nums.count(i)==2:
                ans^=i
        return ans 
        