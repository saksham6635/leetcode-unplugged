class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        #return len(set(nums))>=len(nums)//2
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
            if freq[i]>=3:
                return False
        return True 
    