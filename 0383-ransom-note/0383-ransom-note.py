class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c=0
        a=list(magazine)
        for i in ransomNote:
            if i in a:
                c+=1
                a.remove(i)
        return c==len(ransomNote)
