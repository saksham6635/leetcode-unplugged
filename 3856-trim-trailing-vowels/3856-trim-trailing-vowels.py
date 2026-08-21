class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels={"a","e","i","o","u"}
        s=s[::-1]
        for i in s:
            if i in vowels:
                s=s[1:]
            else:
                break
        return s[::-1]
    
        