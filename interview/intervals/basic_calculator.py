class Solution:
    def calculate(self, s: str) -> int:
        s = list(s.replace(" ", ""))
        
        # Retirar possiveis parenteses e criar expressoes em uma []        
        def remove_parentheses(s):
            expressions = []
            stack = []
            for i in range(len(s)):
                if s[i] == "(":
                    stack.append(i)
                elif s[i] == ")":
                    start = stack.pop()
                    expressions.append(s[start + 1:i])
            if len(expressions) == 0:
                return [s]
            else:
                return expressions

        list_expressions = remove_parentheses(s)
        
        for expression in list_expressions:
            if "(" in expression:
                continue
            
            # Loop para resolver somas e subtrações
            while "+" in expression or "-" in expression:
                for i in range(len(expression)):
                    if expression[i] == "+":
                        expression[i] = int(expression[i-1]) + int(expression[i+1])
                        expression.pop(i-1)
                        expression.pop(i)
                        break
                    elif expression[i] == "-":
                        expression[i] = int(expression[i-1]) - int(expression[i+1])
                        expression.pop(i-1)
                        expression.pop(i)
                        break
                    else:
                        continue

        return expression[0]
