class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        c=0
        d=0
        for i in range(len(nums)):
            if nums[i]<0:
                c+=1
            elif nums[i]>0:
                d+=1
        return max(c,d)


    
        