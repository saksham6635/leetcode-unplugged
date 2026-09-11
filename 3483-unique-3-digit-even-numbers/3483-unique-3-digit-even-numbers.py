class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        l=[0]*10
        ans=0
        for i in digits:
            l[i]+=1
        for i in range(100,1000,2):
            a=i//100
            b=(i//10)%10
            c=i%10
            l[a]-=1
            l[b]-=1
            l[c]-=1
            if l[a]>=0 and l[b]>=0 and l[c]>=0:
                ans+=1
            l[a]+=1
            l[b]+=1
            l[c]+=1
        return ans 


            
        
        