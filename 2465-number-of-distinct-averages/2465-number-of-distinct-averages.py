class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums=sorted(nums)
        distinct=set()
        i,j=0,len(nums)-1
        while i<j:
            avg=(nums[i]+nums[j])/2
            distinct.add(avg)
            i+=1
            j-=1
        return len(distinct)

        