class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        number_stack = []
        operation_stack = []
        res = 0
        
        if len(tokens) == 1:
            return int(tokens[0])
        
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                operation_stack.append(token)
            else:
                number_stack.append(int(token))
                
            while len(number_stack) > 1 and len(operation_stack) > 0:
                num1 = number_stack.pop()
                num2 = number_stack.pop()
                operation = operation_stack.pop()
                
                if operation == '+':
                    res = num1 + num2
                elif operation == '-':
                    res = num2 - num1
                elif operation == '*':
                    res = num1 * num2
                elif operation == '/':
                    res = int(num2 / num1)
                
                number_stack.append(res)
        return res