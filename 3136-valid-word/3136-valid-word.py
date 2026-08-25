class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<=2 or not word.isalnum():
            return False
        vowel,consonant=0,0
        d={'a', 'e', 'i', 'o', 'u',"A","E","I","O","U"}
        for i in word:
            if i.isalpha():
                if i in d:
                    vowel+=1
                else:
                    consonant+=1
        if vowel>=1 and consonant>=1:
            return True
        return False
            

        