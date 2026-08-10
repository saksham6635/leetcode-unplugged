class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        count=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                a=nums[i]|nums[j]
                binary=bin(a)[2:]
                if binary[-1]=="0":
                    count+=1
        if count>0:
            return True
        return False   