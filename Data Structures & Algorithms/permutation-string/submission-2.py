class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        counts1 = [0]*128
        for ch in s1:
            counts1[ord(ch) - ord('A')] +=1

        counts2 = [0]*128

        left =0

        for right,ch in enumerate(s2):

            counts2[ord(ch)-ord('A')] += 1
            if right - left + 1 > len(s1):
                counts2[ord(s2[left])-ord('A')] -= 1
                left = left+1


            if counts1 == counts2:
                return True

        return False
