class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        words=words[left:right+1]
        c=0
        vowels={'a','e','i','o','u'}
        for i in words:
            if i[0] in vowels and i[-1] in vowels:
                c+=1
        return c


        