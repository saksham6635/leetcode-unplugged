class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        s=[str(x) for x in nums]
        s.sort(key=lambda x:x*10,reverse=True)
        a="".join(s)
        b=int(a)
        return str(b)