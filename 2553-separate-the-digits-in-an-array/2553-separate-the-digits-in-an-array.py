class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result=[]
        l=[]
        for i in nums:
            a=str(i)
            l.append(a)
        string="".join(l)
        for i in string:
            result.append(int(i))
        return result
        