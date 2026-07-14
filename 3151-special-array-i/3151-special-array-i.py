class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        c=0
        d=0
        if len(nums)==1:
            return True 
        if nums[0]%2==0:
            for i in range(len(nums)):
                if i%2==0 and nums[i]%2==0:
                    c+=1
                if i%2!=0 and nums[i]%2!=0:
                    d+=1
            if c+d==len(nums):
                return True
            return False 
        else:
            for i in range(len(nums)):
                if i%2==0 and nums[i]%2!=0:
                    c+=1
                if i%2!=0 and nums[i]%2==0:
                    d+=1
            if c+d==len(nums):
                return True
            return False

