class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        nums=sorted(arr)
        res=[]
        if len(nums)<=2:
            return True
        else:
            for i in range(1,len(nums)):
                diff=nums[i]-nums[i-1]
                res.append(diff)
            return len(set(res))==1
        

        