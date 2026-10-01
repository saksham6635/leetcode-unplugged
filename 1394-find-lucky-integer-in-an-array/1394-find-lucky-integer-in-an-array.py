class Solution:
    def findLucky(self, arr: list[int]) -> int:
        f={}
        for i in arr:
            f[i]=f.get(i,0)+1

        values=[]
        for i in f:
            if f[i]==i:
                values.append(i)

        if values:
            return max(values)
        return -1
        