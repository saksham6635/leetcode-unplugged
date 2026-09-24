class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            a=str(nums[i])
            b=list(map(int,a))
            c=sum(b)
            if c==i:
                return i
        return -1