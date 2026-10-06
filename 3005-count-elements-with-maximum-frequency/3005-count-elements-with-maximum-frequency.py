class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq={}
        l=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for i in freq:
            l.append(freq[i])
        return max(l)*l.count(max(l))
        
        