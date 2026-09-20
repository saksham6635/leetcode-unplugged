class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        l=list(s)
        k=[]
        for i in l:
            k.append(123-ord(i))
        for i in range(len(k)):
            deg=k[i]*(i+1)
            ans+=deg
        return ans 
       
