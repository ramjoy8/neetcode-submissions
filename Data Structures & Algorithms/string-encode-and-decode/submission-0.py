class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for each in strs:
            res = res + str(len(each)) + '#' + each
        return res

    def decode(self, s: str) -> List[str]:

        i = 0
        res = []
        while i < len(s):

            j = i

            while s[j]!= '#' and j < len(s):
                j=j+1

            len_word = int(s[i:j])

            res.append(s[j+1:j+1+len_word])

            i = j+1+len_word

        return res



