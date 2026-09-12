class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        s=set()
        for i in range(len(nums)):
            x=nums[i]
            if nums.count(x)==3 and x not in s:
                idx=[j for j,val in enumerate(nums) if val==x]
                if idx[2]-idx[1]==idx[1]-idx[0]:
                    s.add(x)
        return len(s)

        
   
            
        