class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        a=set()
        for i in words:
            l=""
            for j in i:
                l+=code[ord(j)-97]
            a.add(l)
        return len(a)
            
        