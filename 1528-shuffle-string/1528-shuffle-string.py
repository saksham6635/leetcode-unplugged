class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n=len(s)
        t=[""]*n
        for idx,chr in enumerate(s):
            t[indices[idx]]=chr
        return "".join(t)
        