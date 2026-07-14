class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n=len(nums)
        result=[]
        for i in range(n):
            if nums[i]%2==0:
                odd=[x for x in nums[i+1:] if x%2!=0]
                odd_num=len(odd)
                result.append(odd_num)
            else:
                even=[x for x in nums[i+1:] if x%2==0]
                even_num=len(even)
                result.append(even_num)
        return result

        