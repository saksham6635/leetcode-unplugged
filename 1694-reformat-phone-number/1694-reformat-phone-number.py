class Solution:
    def reformatNumber(self, number: str) -> str:
        number=number.replace(" ","")
        number=number.replace("-","")
        t=""
        if len(number)%3==0:
            for i in range(0,len(number),3):
                t+=number[i:i+3]+"-"
            a=list(t)
            a.pop()
            return "".join(a)
        elif len(number)%3==1:
            b=number[:-4]
            c=number[-4:]
            for i in range(0,len(b),3):
                t+=b[i:i+3]+"-"
            return t+c[:2]+"-"+c[2:]
        elif len(number)%3==2:
            b=number[:-2]
            c=number[-2:]
            for i in range(0,len(b),3):
                t+=b[i:i+3]+"-"
            return t+c




        