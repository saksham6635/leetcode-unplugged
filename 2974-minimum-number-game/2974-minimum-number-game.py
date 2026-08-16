class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        a=sorted(nums)
        n=len(nums)
        for i in range(0,n,2):
            a[i],a[i+1]=a[i+1],a[i]
        return a
     



        