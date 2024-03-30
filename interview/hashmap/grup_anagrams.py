# O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        
        return list(anagrams.values())



# class Solution:
#   O(n * mlogm) time complexity
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         hash_map_list = []
#         anagrams = []
        
#         for words in strs:
#             hash_map = {}
#             for word in words:
#                 if word in hash_map:
#                     hash_map[word] += 1
#                 else:
#                     hash_map[word] = 1
#             hash_map_list.append(hash_map)
        
#         for hash_map in hash_map_list:
#             print(hash_map)
#             anagram = []
#             for i in range(len(hash_map_list)):
#                 if hash_map == hash_map_list[i]:
#                     anagram.append(strs[i])
                    
#             if anagram not in anagrams:
#                 anagrams.append(anagram)  
        
#         return anagrams