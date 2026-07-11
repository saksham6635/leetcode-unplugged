class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            binary=bin(i)[2:]
            l.append(binary)
        bin1=l[0]+l[1]+l[2]
        num1=int(bin1,2)
        bin2=l[0]+l[2]+l[1]
        num2=int(bin2,2)
        bin3=l[1]+l[0]+l[2]
        num3=int(bin3,2)
        bin4=l[1]+l[2]+l[0]
        num4=int(bin4,2)
        bin5=l[2]+l[0]+l[1]
        num5=int(bin5,2)
        bin6=l[2]+l[1]+l[0]
        num6=int(bin6,2)
        return max([num1,num2,num3,num4,num5,num6])