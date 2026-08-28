class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result=[]
        while len(heights)>0:
            max_height=max(heights)
            idx=heights.index(max_height)
            tallest=names[idx]
            result.append(tallest)
            heights.pop(idx)
            names.pop(idx)
        return result

       
         