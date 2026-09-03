class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        f1={}
        f2={}
        for i in words1:
            f1[i]=f1.get(i,0)+ 1
        for i in words2:
            f2[i]=f2.get(i,0)+1
        count=0
        for i in f1:
            if f1[i]==1 and f2.get(i,0)==1:
                count+=1
        return count
    

        