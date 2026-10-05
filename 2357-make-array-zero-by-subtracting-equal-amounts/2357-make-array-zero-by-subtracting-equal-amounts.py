class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        seen=[x for x in nums if x!=0]
        return len(set(seen))
       

        