class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        c=0
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1
        for i in f:
            if i+k in f:
                c+=f[i]*f[i+k]
        return c
        