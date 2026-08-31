class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        result=[]
        for l in matrix:
            result.append(sum(l))
        return result        