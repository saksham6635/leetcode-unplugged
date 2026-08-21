class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq={}
        n=len(nums)
        for i in nums:
            freq[i]=freq.get(i,0)+1
        ans=[x for x,count in freq.items() if count>n//3]
        return ans 

