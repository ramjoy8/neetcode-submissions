class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = {}
        for each in t:
            need[each] = need.get(each,0) +1

        have = {}

        need_count = len(need)
        have_count = 0
        min_len = float('inf')
        min_res = ''
        left =0
        for right,ch in enumerate(s):

            have[ch] = have.get(ch,0) + 1

            if ch in need and need[ch] == have[ch]:
                have_count +=1

            while have_count == need_count:

                if right-left+1 < min_len:
                    min_len = right-left+1
                    min_res = s[left:right+1]

                left_char = s[left]
                have[left_char] -= 1

                if left_char in need and need[left_char] > have[left_char]:
                    have_count -= 1

                left = left +1

        return min_res        




