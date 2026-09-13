class Solution:
    def longestPalindrome(self, s: str) -> int:
        l=[]
        f={}
        if s==s[::-1]:
            return len(s)
        for i in s:
            f[i]=f.get(i,0)+1
        odd=False
        for i in f:
            if f[i]%2==0:
                l.append(f[i])
            else:
                l.append(f[i]-1)
                odd=True
        if odd==True:
            return sum(l)+1
        return sum(l)

         
        


            

        

        