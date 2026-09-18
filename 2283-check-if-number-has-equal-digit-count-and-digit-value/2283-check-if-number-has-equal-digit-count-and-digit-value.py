class Solution:
    def digitCount(self, num: str) -> bool:
        c=0
        for i in range(len(num)):
            if num.count(str(i))==int(num[i]):
                c+=1
        return c==len(num)
        
        