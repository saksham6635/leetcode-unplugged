class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        max_element=max(nums)
        min_element=min(nums)
        idx1=nums.index(max_element)
        idx2=nums.index(min_element)
        front=max(idx1,idx2)+1
        back=n-min(idx1,idx2)
        a=min(idx1+1,n-idx1)
        b=min(idx2+1,n-idx2)
        return min(front,back,a+b)
