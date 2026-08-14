class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        arr1=[]
        arr2=[]
        max_element=max(nums)
        min_element=min(nums)
        c=0
        for i in range(-k,k+1):
            arr1.append(max_element-i)
            arr2.append(min_element+i)
        c=max(c,min(arr1)-max(arr2))
        return c


        