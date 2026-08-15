class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        if n*[0]==nums:
            return 0
        for i in nums:
            c^=i
        if c!=0:
            return n
        else:
            return n-1
        