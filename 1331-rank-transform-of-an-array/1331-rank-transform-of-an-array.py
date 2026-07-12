class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a=sorted(set(arr))
        dict_={x:i+1 for i,x in enumerate(a)}
        stack=[]
        for i in arr:
            stack.append(dict_[i])
        return stack