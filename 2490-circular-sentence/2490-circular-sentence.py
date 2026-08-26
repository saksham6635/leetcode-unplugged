class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        a=sentence.split()
        n=len(a)
        c=0
        for i in range(n):
            if a[i][-1]==a[(i+1)%n][0]:
                c+=1
        return c==n
        