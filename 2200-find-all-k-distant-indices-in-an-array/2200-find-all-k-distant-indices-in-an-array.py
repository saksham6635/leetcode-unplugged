class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        l,m=[],[]
        j=0
        n=len(nums)
        for i in range(len(nums)):
            if nums[i]==key:
                l.append(i)
        for i in l:
            j=0
            while j<n:
                if abs(j-i)<=k:
                    m.append(j)
                j+=1
        return sorted(set(m))
        
