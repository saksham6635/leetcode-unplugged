class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        a=set(nums)
        b=[x for x in a if x!=0]
        return len(b)

        