class Solution:
    def generateTag(self, caption: str) -> str:
        a=caption.title()
        b=a.split()
        if b:
            b[0]=b[0].lower()
        c="".join(map(str,b))
        t="#"+c
        s="#"
        for i in t[1:]:
            if i.isalpha() and i.isascii():
                s+=i
        return s[:100]


        