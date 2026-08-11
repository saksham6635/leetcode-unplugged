class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans=0
        n=len(nums)
        for i in range(n):
            binary=bin(i)[2:]
            count=binary.count("1")
            if count==k:
                ans+=nums[i]
        return ans 

        