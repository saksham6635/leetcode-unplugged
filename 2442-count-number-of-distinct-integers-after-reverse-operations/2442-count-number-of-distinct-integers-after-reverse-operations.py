class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        reverse=[]
        for i in nums:
            b=""
            while i>0:
                a=str(i%10)
                i//=10
                b+=a
            reverse.append(int(b))
        return len(set(nums+reverse))
    
        