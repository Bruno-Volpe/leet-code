class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        teste = []
        
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = [t[i], 1]  # If the character is not in the dictionary, add it with count 1
            else:
                s_dict[s[i]][1] += 1  # If it's already in the dictionary, increase the count
        
        for i in range(len(t)):
            if s_dict.get(s[i]) and s_dict[s[i]][1] >= 1:
                teste.append(s_dict[s[i]][0])
                s_dict[s[i]][1] -= 1  # Reduce the count of occurrences
            
        return teste == list(t)
