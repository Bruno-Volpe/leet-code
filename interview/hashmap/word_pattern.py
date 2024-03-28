class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_map = {}
        s_arr = s.split(' ')
        
        if len(pattern) != len(s_arr):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in hash_map and s_arr[i] not in hash_map.values():
                hash_map[pattern[i]] = s_arr[i]
                
        new_str = ''
        
        for i in range(len(pattern)):
            if pattern[i] not in hash_map:
                return False
            new_str += hash_map[pattern[i]] + ' '
        
            
        return new_str.strip() == s