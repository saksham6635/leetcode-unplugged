class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        a=startTime[:2]
        b=endTime[:2]
        c=startTime[3:5]
        d=endTime[3:5]
        e=endTime[6:]
        f=startTime[6:]
        if a==b and d==c and e==f:
            return 0
        if a==b and c==d and e!=f:
            return int(e)-int(f)
        elif a==b and c!=d:
            if int(e)>=int(f):
                return (int(d)-int(c))*60+int(e)-int(f)
            else:
                return (int(d)-int(c)-1)*60+60-int(f)+int(e)
        elif a!=b:
            if int(d)>=int(c) and int(e)>=int(f):
                return (int(b)-int(a))*3600+(int(d)-int(c))*60+int(e)-int(f)
            if int(d)>=int(c) and int(e)<int(f):
                return (int(b)-int(a))*3600+(int(d)-int(c)-1)*60+60-int(f)+int(e)
            if int(d)<int(c) and int(e)>=int(f):
                return (int(b)-int(a)-1)*3600+(60-int(c)+int(d))*60+int(e)-int(f) 
            if int(d)<int(c) and int(e)<int(f):
                return (int(b)-int(a)-1)*3600+(60-int(c)+int(d)-1)*60+int(e)-int(f)+60
    
    
        
            
        