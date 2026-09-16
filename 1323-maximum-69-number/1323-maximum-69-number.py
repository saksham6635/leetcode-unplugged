class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        n=len(s)
        l=[]
        for i in range(n):
            if s[i]=="9":
                l.append(s[i])
            else:
                l.append("9")
                break
        a=len(l)
        l.append(s[a:])
        
        new="".join(l)
        return int(new)

            
       

        