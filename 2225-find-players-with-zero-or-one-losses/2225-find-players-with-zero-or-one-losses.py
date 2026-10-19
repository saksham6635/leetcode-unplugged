class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        winner=[]
        loser=[]
        for i in range(len(matches)):
            winner.append(matches[i][0])
            loser.append(matches[i][1])
        win=set(winner)
        lose=set(loser)
        a=sorted(list(win-lose))
        f={}
        for i in loser:
            f[i]=f.get(i,0)+1
        b=[]
        for i in f:
            if f[i]==1:
                b.append(i)
        l=[]
        l.append(a)
        l.append(sorted(b))
        return l
    
        


        