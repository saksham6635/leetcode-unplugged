class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        max_num=max(nums)
        min_num=min(nums)
        nums_set=set(nums)
        result=[]
        for i in range(min_num,max_num+1):
            if i not in nums_set:
                result.append(i)
        return result