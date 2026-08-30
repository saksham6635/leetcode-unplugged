class Solution:
    def judgeCircle(self, moves: str) -> bool:
        left=moves.count("L")
        right=moves.count("R")
        up=moves.count("U")
        down=moves.count("D")
        if up==down and left==right:
            return True
        return False

        