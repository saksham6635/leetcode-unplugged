class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        else:
            for i in range(len(word)):
                if word[i]==ch:
                    idx=i
                    break
            result=word[:idx+1][::-1]+word[idx+1:]
            return result
        