class Solution:
    def greatestLetter(self, s: str) -> str:
        upper = set()
        lower = set()
        for ch in s:
            if ch.isupper():
                upper.add(ch)
            else:
                lower.add(ch)
        common = [ch for ch in upper if ch.lower() in lower]
        if not common:
            return ""
        return max(common)
