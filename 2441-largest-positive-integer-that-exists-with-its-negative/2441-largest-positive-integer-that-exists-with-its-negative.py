class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        a=float("-inf")
        for i in nums:
            if i in nums and i*-1 in nums:
                a=max(a,i)
        return -1 if a==float('-inf') else a

        