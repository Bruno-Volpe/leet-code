class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strArr = s.split()
        if len(strArr) == 0:
            return 0
    
        return len(strArr[-1])