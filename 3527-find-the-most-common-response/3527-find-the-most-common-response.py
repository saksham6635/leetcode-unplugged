class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        seen=[]
        for i in responses:
            for j in set(i):
                seen.append(j)
        
        freq={}
        for word in seen:
            freq[word]=freq.get(word,0)+1
        max_key=max(freq,key=freq.get)

        l=[]
        for i in freq:
            if freq[i]==freq[max_key]:
                l.append(i)
        if l:
            return min(l)
        return ""
    

        


        