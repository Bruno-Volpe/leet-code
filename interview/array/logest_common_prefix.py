class Solution:  
    def getPrefix(self, a: str, b: str) -> str:
        prefix = ""
        for i in range(min(len(a), len(b))):
            if a[i] == b[i]:
                prefix += a[i]
            else:
                break
        return prefix  

    def longestCommonPrefix(self, strs: List[str]) -> str:        
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        
        prefix = strs[0]
        for i in range(1, len(strs)):
            prefix = self.getPrefix(prefix, strs[i])
        return prefix
