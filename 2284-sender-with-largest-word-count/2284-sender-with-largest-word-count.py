class Solution:
    def largestWordCount(self, messages: list[str], senders: list[str]) -> str:
        words=[]
        for i in messages:
            a=i.split()
            b=len(a)
            words.append(b)
        d={}
        for i in range(len(senders)):
            if senders[i]  not in d:
                d[senders[i]]=words[i]
            else:
                d[senders[i]]+=words[i]
        max_word=max(d.values())
        l=[]
        for i in d:
            if d[i]==max_word:
                l.append(i)
        return max(l)

        