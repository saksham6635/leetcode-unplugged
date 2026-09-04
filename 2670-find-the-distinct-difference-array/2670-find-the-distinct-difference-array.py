class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        diff_arr=[]
        for i in range(len(nums)):
            a=len(set(nums[:i+1]))
            b=len(set(nums[i+1:]))
            diff_arr.append(a-b)
        return diff_arr
    
        