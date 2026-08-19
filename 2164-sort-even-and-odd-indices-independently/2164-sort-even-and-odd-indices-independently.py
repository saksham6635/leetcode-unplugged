class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        result=[]
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        for i in range(len(even)):
            result.append(even[i])
            if i<len(odd):
                result.append(odd[i])
        return result
