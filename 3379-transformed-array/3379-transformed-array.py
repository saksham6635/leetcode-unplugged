class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result=[]
        n=len(nums)
        for i in range(n):
            if nums[i]!=0:
                new_value=nums[(i+nums[i])%n]
            else:
                new_value=nums[i]         
            result.append(new_value)
        return result
        