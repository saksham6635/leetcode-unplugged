class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(len(nums)):
            prefix=sum(nums[:i+1])
            suffix=sum(nums[i:])
            if prefix==suffix:
                return i
                break
        return -1
        