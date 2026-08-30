class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        l=[]
        for i in range(len(nums)):
            if nums[i]==target:
                a=abs(i-start)
                l.append(a)
        return min(l)