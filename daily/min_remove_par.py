class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        new_s = []
        s_arr = list(s)
        
        for s in range(len(s_arr)):
            if s_arr[s] == '(':
                count += 1
            elif s_arr[s] == ')':
                if count <= 0:
                    s_arr[s] = ''
                else:
                    count -= 1
            
            new_s.append(s_arr[s])
            
            
        if count > 0:
            for i in range(len(new_s) - 1, -1, -1):
                if new_s[i] == '(' and count > 0:
                    new_s[i] = ''
                    count -= 1
                
        return ''.join(new_s)