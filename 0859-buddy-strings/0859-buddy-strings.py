class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        c=0
        f1={}
        f2={}
        for i in s:
            f1[i]=f1.get(i,0)+1
        for i in goal:
            f2[i]=f2.get(i,0)+1
        if f1!=f2:
            return False
        for i in range(len(s)):
            if s[i]!=goal[i]:
                c+=1
        if c==2:
            return True
        elif c==0 and len(set(s))==len(s):
            return False
        elif c==0 and len(set(s))!=len(s):
            return True
        else:
            return False
