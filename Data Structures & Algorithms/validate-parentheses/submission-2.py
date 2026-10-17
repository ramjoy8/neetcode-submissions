class Solution:
    def isValid(self, s: str) -> bool:
        
        open = ('[','{','(')

        tmp = []

        for each in s:

            if each in open:

                tmp.append(each)
            elif not tmp:
                return False

            elif each == ']':

                last = tmp.pop()
                if last!='[':
                    return False

            elif each == '}':
                last = tmp.pop()
                if last!='{':
                    return False
            elif each == ')' :
                last = tmp.pop()
                if last!='(':
                    return False


        if not tmp:
            return True
        else:
            return False
            