import math
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                gcd=math.gcd(nums[i],nums[j])
                strength=nums[i]*nums[j]//(gcd*gcd)
                ans=max(ans,strength)
        return ans 
        