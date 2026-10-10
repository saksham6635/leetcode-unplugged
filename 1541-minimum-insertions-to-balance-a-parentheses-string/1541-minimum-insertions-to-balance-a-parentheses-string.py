class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0   # total insertions needed
        need = 0  # number of ')' needed to balance so far
        i = 0
        while i < len(s):
            if s[i] == '(':
                need += 2
                if need % 2 == 1:  # odd, need one more ')'
                    res += 1
                    need -= 1
            else:  # s[i] == ')'
                need -= 1
                if need < 0:  # too many ')'
                    res += 1
                    need = 1
            i += 1
        return res + need
