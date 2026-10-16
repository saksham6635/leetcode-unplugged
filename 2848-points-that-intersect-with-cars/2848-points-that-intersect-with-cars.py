class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        arr=[0]*101
        for start,end in nums:
            arr[start:end+1]=[1]*(end-start+1)
        return sum(arr)
        