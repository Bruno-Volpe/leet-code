class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        teste = []
        
        for i in range(len(s)):
            s_dict[s[i]] = t[i]
        
        for i in range(len(t)):
            teste.append(s_dict[s[i]])
            
        return teste == list(t)
        