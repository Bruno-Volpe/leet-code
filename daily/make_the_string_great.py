class Solution:
    def makeGood(self, s: str) -> str:
        s_arr = list(s)
        
        for i in range(len(s_arr) - 1):
            if s_arr[i].lower() == s_arr[i + 1].lower() and s_arr[i] != s_arr[i + 1]:
                s_arr[i] = ''
                s_arr[i + 1] = ''
                return self.makeGood("".join(s_arr))
        
        return "".join(s_arr)