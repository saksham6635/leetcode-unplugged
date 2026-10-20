class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        reverse=[]
        for i in nums:
            a=int(str(i)[::-1])
            reverse.append(a)
        return len(set(reverse+nums))
    
        