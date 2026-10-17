class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        lonely=[]
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for i in freq:
            if freq[i]==1:
                if (i+1) not in freq and (i-1) not in freq:
                    lonely.append(i)
        return lonely
            