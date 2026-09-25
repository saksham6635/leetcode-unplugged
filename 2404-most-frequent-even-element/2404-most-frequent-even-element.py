class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        f={}
        l,m=[],[]
        for num in nums:
            f[num]=f.get(num,0)+1            
        for i in f:
            if i%2==0:
                l.append(f[i])
        if not l:
            return -1
        else:
            high=max(l)
        for i in f:
            if  i%2==0 and f[i]==high:
                m.append(i)
        return min(m)



        

        