class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        #counter-subaaray sums
        #hashset-check the sums are equal
        n=len(nums)
        l=[]
        for i in range(n):
            for j in range(i,n):
                subarr=nums[i:j+1]
                if len(subarr)==2:
                    l.append(sum(subarr))
        return len(l)!=len(set(l))


        