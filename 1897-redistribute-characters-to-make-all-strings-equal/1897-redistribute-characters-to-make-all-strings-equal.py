class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        string="".join(words)
        n=len(words)
        f={}
        l=[]
        for i in string:
            f[i]=f.get(i,0)+1
        for i in f:
            l.append(f[i]%n)
        return set(l)=={0}
        
