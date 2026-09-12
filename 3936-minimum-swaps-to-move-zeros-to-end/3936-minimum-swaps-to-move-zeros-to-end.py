class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        zero=nums.count(0)
        n=len(nums)
        swaps=0
        for i in range(n-zero,n):
            if nums[i]!=0:
                swaps+=1
        return swaps 
       


     
        