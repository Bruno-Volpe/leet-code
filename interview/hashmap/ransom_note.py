# Definindo a classe Solution
class Solution:
    # Definindo a função canConstruct que recebe duas strings como parâmetros
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Inicializando um dicionário vazio para contar a frequência de cada caractere
        char_count = {}
        # Iterando sobre cada caractere na string 'magazine'
        for char in magazine:
            # Se o caractere já está no dicionário, incrementa a contagem
            if char in char_count:
                char_count[char] += 1
            # Se o caractere não está no dicionário, adiciona com a contagem 1
            else:
                char_count[char] = 1

        # Iterando sobre cada caractere na string 'ransomNote'
        for char in ransomNote:
            # Se o caractere não está no dicionário ou a contagem é 0, retorna False
            if char not in char_count or char_count[char] <= 0:
                return False
            # Se o caractere está no dicionário e a contagem é maior que 0, decrementa a contagem
            char_count[char] -= 1

        # Se todas as letras da 'ransomNote' estão na 'magazine', retorna True
        return True