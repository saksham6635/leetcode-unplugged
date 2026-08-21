class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        n=len(nums)
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=[x for x in d if d[x]>n//3]
        return ans 
        
