class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s="123456789"
        n=9
        result=[]
        for i in range(9):
            for j in range(i+1,10):
                k=int(s[i:j])
                if k in range(low,high+1):
                    result.append(k)
        return sorted(result)
        