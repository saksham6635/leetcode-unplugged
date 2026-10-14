class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        words1=s1.split()
        words2=s2.split()
        l=[]
        f1={}
        f2={}
        for i in words1:
            f1[i]=f1.get(i,0)+1
        for i in words2:
            f2[i]=f2.get(i,0)+1
        for i in f1:
            if f1[i]==1 and i not in f2:
                l.append(i)
        for i in f2:
            if f2[i]==1 and i not in f1:
                l.append(i)
        return l

        