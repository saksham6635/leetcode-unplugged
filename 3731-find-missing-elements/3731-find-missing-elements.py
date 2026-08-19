class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        max_num=max(nums)
        min_num=min(nums)
        result=[]
        for i in range(min_num,max_num+1):
            if i not in nums:
                result.append(i)
        return sorted(result)