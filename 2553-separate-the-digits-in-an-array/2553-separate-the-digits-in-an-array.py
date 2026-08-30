class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result=[]
        l=[]
        for i in nums:
            a=str(i)
            l.append(a)
        string="".join(l)
        b=list(map(int,string))
        return b
        
        