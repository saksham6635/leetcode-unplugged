class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        seen=[0]*26
        for i in key:
            if i in seen or i==" ":
                continue
            seen.append(i)
        mapping=[chr(97+i) for i in range(26)]
        a=seen[26:]
        decoded=[]
        for i in message:
            if i==" ":
                decoded.append(" ")
            else:
                decoded.append(mapping[a.index(i)])
        return "".join(decoded)


       
        




        