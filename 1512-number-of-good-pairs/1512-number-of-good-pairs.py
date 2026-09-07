class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for i in freq:
            n=freq[i]
            if n>1:
                count+= ((n)*(n-1))//2
        return count
        

        