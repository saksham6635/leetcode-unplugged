class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        seen = {}
        used = {}
        c = 0
        for w, p in zip(words, pattern):
            if w not in seen:
                if p in used:  
                    return False
                c += 1
                seen[w] = p
                used[p] = w
            else:
                if seen[w] != p:   
                    return False
        return True
