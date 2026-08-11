class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans=0
        bin1=bin(x)[2:]
        bin2=bin(y)[2:]
        length=max(len(bin1),len(bin2))
        bin1=bin1.zfill(length)
        bin2=bin2.zfill(length)
        for i in range(length):
            if bin1[i]!=bin2[i]:
                ans+=1
        return ans 
        