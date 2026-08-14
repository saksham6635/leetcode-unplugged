class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            count = {}
            for j in range(i, len(s)):
                if s[j] in count:
                    count[s[j]] += 1
                else:
                    count[s[j]] = 1
                if count[s[j]] > 2:
                    break
                ans = max(ans, j - i + 1)
        return ans