class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        sq1={"a","c","e","g"}
        sq2={"b","d","f","h"}
        if  coordinate1[0] in  sq1 and  coordinate2[0] in sq1:
            if int(coordinate1[1])%2==int(coordinate2[1])%2:
                return True 
            else:
                return False
        elif coordinate1[0] in sq2 and coordinate2[0] in sq2:
            if int(coordinate1[1])%2==int(coordinate2[1])%2:
                return True 
            else:
                return False
        else:
            if int(coordinate1[1])%2==int(coordinate2[1])%2:
                return False
            else:
                return True



        