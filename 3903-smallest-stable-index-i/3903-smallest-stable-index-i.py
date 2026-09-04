class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            max_element=max(nums[:i+1])
            min_element=min(nums[i:])
            diff=max_element-min_element
            if diff<=k:
                return i
        return -1