class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen=set(words)
        pairs=0
        for w in words:
            rev=w[::-1]
            if rev in seen and rev!=w:
                pairs+=1
                seen.remove(w)
                seen.remove(rev)
        return pairs

      
        
        