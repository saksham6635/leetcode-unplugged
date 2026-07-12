class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_arr=sorted(nums)
        stack=[]
        for i in range(len(sorted_arr)):
            if sorted_arr[i]==target:
                stack.append(i)
        return stack