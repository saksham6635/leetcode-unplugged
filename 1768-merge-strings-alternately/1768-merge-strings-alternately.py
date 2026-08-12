class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        length=min(len(word1),len(word2))
        if len(word1)>=len(word2):
            c=word1
        else:
            c=word2
        for i in range(length):
            result+=word1[i]
            result+=word2[i]
        remaining=c[i+1:]
        return result+remaining
        

        