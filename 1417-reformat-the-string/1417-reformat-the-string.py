class Solution:
    def reformat(self, s: str) -> str:
        al,num=0,0
        arr1,arr2=[],[]
        t=""
        for i in s:
            if i.isdigit():
                num+=1
                arr1.append(i)
            else:
                al+=1
                arr2.append(i)
        if num-al not in {1,0,-1}:
            return ""
        else:
            if al-num==1:
                for i in range(len(arr2)-1):
                    t+=arr2[i]+arr1[i]
                return t+arr2[-1]
            elif al-num==-1:
                for i in range(len(arr1)-1):
                    t+=arr1[i]+arr2[i]
                return t+arr1[-1]
            elif al-num==0:
                for i in range(len(arr1)):
                    t+=arr1[i]+arr2[i]
                return t

                    

        