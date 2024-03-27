class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n) and O(n)
        hash_map = {}
        # letra corresponde a chave e a quantidade de vezes que aparece na string
        for letter in s:
            if letter in hash_map:
                hash_map[letter] += 1
            else:
                hash_map[letter] = 1
        
        for letter in t:
            if letter in hash_map:
                hash_map[letter] -= 1
            else:
                return False
        
        for key in hash_map:
            if hash_map[key] != 0:
                return False
            
        return True

# class Solution:
    #A de cima roda mttttt melhor
    # Time complexity: O(n^2), because list.remove() is an O(n) operation

#     def isAnagram(self, s: str, t: str) -> bool:
#         original_word_arr = list(s)
#         arr = list(t)
        
#         for char in t:
#             if char in original_word_arr:
#                 arr.remove(char)
#                 original_word_arr.remove(char)
            
#         return len(arr) == 0 and len(original_word_arr) == 0