class Solution:
    def countElements(self, nums: list[int]) -> int:
        a=max(nums)
        b=min(nums)
        c=0
        for i in nums:
            if (i!=a and i<a) and (i!=b and i>b):
                c+=1
        return c


        