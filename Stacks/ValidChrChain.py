class Solution:
    def isValid(self, s: str) -> bool:
        brackets = list(s)
        print(brackets)
        print(len(brackets))
        while len(brackets) > 0:
            #ASCII number for characters
            if ord(brackets.pop()) - ord(brackets.pop()) > 3:
                return False
            else: self.isValid(brackets)
        return True
Solution()