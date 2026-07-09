class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n=len(s)
        result=""
        for i in range(len(s)):
            result+=s[(i+k)%n]
        return result