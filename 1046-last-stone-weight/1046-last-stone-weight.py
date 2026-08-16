class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n=len(stones)
        arr=sorted(stones)
        while len(arr)>1:
            if arr[-1]==arr[-2]:
                arr.pop()
                arr.pop()
            else:
                arr[-1]=abs(arr[-1]-arr[-2])
                arr.pop(-2)
            arr.sort()
        if len(arr)==0:
            return 0
        return arr[0]


        