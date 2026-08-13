class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        arr=sorted(nums)
        result=(arr[-1]-1)*(arr[-2]-1)
        return result

        