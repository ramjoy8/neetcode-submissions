class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0

        count = [0]*26
        max_freq = 0
        res =0
        for right,ch in enumerate(s):

            count[ord(ch) - ord('A')] +=1

            max_freq = max(max_freq, count[ord(ch) - ord('A')])
            while right-left+1 > k+max_freq:
                count[ord(s[left]) - ord('A')] = count[ord(s[left]) - ord('A')] -1 
                left = left+1

            res = max(res, right-left+1)
        return res