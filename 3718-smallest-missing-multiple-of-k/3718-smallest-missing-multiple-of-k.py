class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        l=[]
        max_element=max(nums)
        for i in range(k,max_element+k+1):
            if i%k==0 and i not in nums:
                l.append(i)
        return min(l)
                
                
        