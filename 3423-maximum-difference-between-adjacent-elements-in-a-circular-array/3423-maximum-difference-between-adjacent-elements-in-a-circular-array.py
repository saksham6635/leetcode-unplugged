class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        stack=[]
        for i in range(len(nums)):
            diff=abs(nums[i]-nums[i-1])
            stack.append(diff)
        return max(stack)
        