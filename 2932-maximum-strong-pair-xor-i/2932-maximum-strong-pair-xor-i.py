class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        l,m=[],[]
        n=len(nums)
        c=0
        for i in range(n):
            for j in range(i,n):
                if abs(nums[i]-nums[j])<=min(nums[i],nums[j]):
                    l.append(nums[i])
                    m.append(nums[j])
        for i in range(len(l)):
            a=l[i]^m[i]
            c=max(a,c)
        return c

        