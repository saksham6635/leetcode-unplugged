class Solution:
    def maxFreqSum(self, s: str) -> int:
        d={'a', 'e', 'i', 'o', 'u'}
        vowel=[0]*26
        consonant=[0]*26
        for i in s:
            idx=ord(i)-97
            if i in d:
                vowel[idx]+=1
            else:
                consonant[idx]+=1
        return max(vowel)+max(consonant)       
            
        