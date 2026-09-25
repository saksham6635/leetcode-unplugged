import heapq

class Solution:

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        f = {}

        for i in words:
            f[i] = f.get(i, 0) + 1

        a=sorted(f,key=lambda word: (-f[word], word))
        return a[:k]