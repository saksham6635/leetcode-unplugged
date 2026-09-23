class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        ops=0
        c=0
        l=[]
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1
        for i in f:
            if f[i]%2==0:
                ops+=f[i]//2
            else:
                ops+=f[i]//2
                c+=1
        l.append(ops)
        l.append(c)
        return l
        

        