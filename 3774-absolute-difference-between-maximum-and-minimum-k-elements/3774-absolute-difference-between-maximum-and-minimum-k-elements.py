class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        sort=sorted(nums)
        prefix_sum=sum(sort[:k])
        suffix_sum=sum(sort[-k:])
        return abs(prefix_sum-suffix_sum)
        