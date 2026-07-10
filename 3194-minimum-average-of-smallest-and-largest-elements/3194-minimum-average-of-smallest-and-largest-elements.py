class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        sort=sorted(nums)
        stack=[]
        n=len(nums)
        for i in range(n//2):
            avg=(sort[i]+sort[n-1-i])/2
            stack.append(avg)
        return min(stack)
        