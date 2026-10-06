class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count_s = [0]*128
        count_t = [0]*128

        for each in s:
            count_s[ord(each)- ord('a')] +=1

        for each in t:
            count_t[ord(each)- ord('a')] +=1

        if count_s == count_t:
            return True

        return False


