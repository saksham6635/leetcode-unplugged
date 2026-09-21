class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        l=[]
        c=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                k=s[i:j]
                if len(k)==2:
                    l.append(k)
        for i in l:
            if i in s[::-1]:
                c+=1
                break
        return c==1
        