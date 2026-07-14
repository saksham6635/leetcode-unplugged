class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        str_num=str(n)
        rev=str_num[::-1]
        rev_num=int(rev)
        result=[]
        a=max(n,rev_num)
        b=min(n,rev_num)
        for i in range(b,a+1):
            if i>1:
                isPrime=True
                for num in range(2,int(i**0.5)+1):
                    if i%num==0:
                        isPrime=False
                        break
                if isPrime:
                    result.append(i)
        return sum(result)
        

        