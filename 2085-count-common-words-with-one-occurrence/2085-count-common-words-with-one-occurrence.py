class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        a=set()
        b=set()
        for i in set(words1):
            if words1.count(i)==1:
                a.add(i)
        for i in set(words2):
            if words2.count(i)==1:
                b.add(i)
        return len(a.intersection(b))

        