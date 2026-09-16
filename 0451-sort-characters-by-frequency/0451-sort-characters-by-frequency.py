class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        return ''.join(ch * count for ch, count in sorted_items)

        

        