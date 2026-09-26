class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        seen={}
        ans=float("inf")
        for i,a in enumerate(cards):
            if  a in seen:
                if i-seen[a]+1 <ans:
                    ans=i-seen[a]+1
            seen[a]=i
        return -1 if ans==float("inf") else ans



        