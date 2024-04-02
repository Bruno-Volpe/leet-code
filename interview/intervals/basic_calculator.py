class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        
        # Função para avaliar expressões dentro de parênteses
        def evaluate_expression(expression):
            total = 0
            operand = 0
            sign = 1
            i = 0
            while i < len(expression):
                char = expression[i]
                if char.isdigit():
                    operand = operand * 10 + int(char)
                elif char == "+":
                    total += sign * operand
                    operand = 0
                    sign = 1
                elif char == "-":
                    total += sign * operand
                    operand = 0
                    sign = -1
                elif char == "(":
                    j = i + 1
                    count = 1
                    while count != 0:
                        if expression[j] == "(":
                            count += 1
                        elif expression[j] == ")":
                            count -= 1
                        j += 1
                    operand = evaluate_expression(expression[i+1:j-1])
                    i = j - 1
                i += 1
            return total + sign * operand
        
        return evaluate_expression(s)
