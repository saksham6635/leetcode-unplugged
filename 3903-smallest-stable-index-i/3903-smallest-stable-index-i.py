class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        ans=float('inf')
        prefix,suffix=[],[]
        for i in range(1,len(nums)+1):
            prefix.append(max(nums[:i]))
        for i in range(len(nums)):
            suffix.append(min(nums[i:]))
        for i in range(len(prefix)):
            score=prefix[i]-suffix[i]
            if score<=k:
                ans=min(ans,i)
        return ans if ans!=float('inf') else -1
           
        
        


        