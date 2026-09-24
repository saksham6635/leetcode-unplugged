class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        c=0
        for i in nums:
            if i+diff in nums and i+2*diff in nums:
                c+=1
        return c
        