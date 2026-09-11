class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        a=sorted(nums)
        n=len(nums)
        b=float('-inf')
        for i in range(n//2):
            b=max(b,a[i]+a[n-1-i])
        return b
        