class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_arr = list(s)
        t_arr = list(t)
        
        for el in t_arr:
            if s_arr and s_arr[0] == el:
                s_arr.pop(0)
                
        return not s_arr