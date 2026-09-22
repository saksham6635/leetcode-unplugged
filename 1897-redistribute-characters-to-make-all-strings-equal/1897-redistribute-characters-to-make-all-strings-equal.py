class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        string="".join(words)
        n=len(words)
        f={}
        l=[]
        for i in string:
            f[i]=f.get(i,0)+1
        equal=True
        for i in f:    
            if f[i]%n==0:
                equal=True
            else:
                equal=False
                break
        if equal==False:
            return False
        return True

        
