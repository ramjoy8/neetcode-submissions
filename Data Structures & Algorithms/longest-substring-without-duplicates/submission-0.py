class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}

        left = 0
        right = 0
        res = 0

        for right in range(len(s)):
            if s[right] in last_seen and last_seen[s[right]] >= left:
                left = last_seen[s[right]] + 1

            last_seen[s[right]] = right

            res = max(res, right-left+1)

        return res