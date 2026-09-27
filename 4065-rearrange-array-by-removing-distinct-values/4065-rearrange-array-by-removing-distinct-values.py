class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        l=[]
        while len(nums)!=0:
            a=sorted(set(nums))
            l.extend(a)
            for i in a:
                nums.remove(i)
        return l
            
        