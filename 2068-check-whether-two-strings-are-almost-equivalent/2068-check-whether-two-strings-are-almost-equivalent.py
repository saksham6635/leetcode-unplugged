class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        arr1=[0]*26
        arr2=[0]*26
        for i in word1:
            idx=ord(i)-97
            arr1[idx]+=1
        for i in word2:
            idx=ord(i)-97
            arr2[idx]+=1
        for i in range(26):
            diff=abs(arr1[i]-arr2[i])
            if diff>3:
                return False
        return True 

        