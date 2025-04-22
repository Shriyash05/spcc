class TACGenerator:
    def __init__(self):
        self.temp_count = 1  # Counter for temporary variables
        self.tac = []  # List to store TAC instructions

    def generate_tac(self, expr):
        """Generate three address code for a given expression"""
        tokens = expr.split()
        self.expr_to_tac(tokens)

    def expr_to_tac(self, tokens):
        """Convert expression to TAC"""
        stack = []

        for token in tokens:
            if token.isdigit():  # if it's a number
                stack.append(token)
            elif token.isidentifier():  # if it's a variable
                stack.append(token)
            elif token in '+-*/':  # if it's an operator
                operand2 = stack.pop()
                operand1 = stack.pop()
                temp_var = f't{self.temp_count}'
                self.temp_count += 1

                # Generate TAC instruction
                self.tac.append(f'{temp_var} = {operand1} {token} {operand2}')
                stack.append(temp_var)

        return stack[-1]  # Return the result

    def print_tac(self):
        """Print generated TAC"""
        print("\nThree Address Code:")
        for line in self.tac:
            print(line)


# Example usage
expr = "b + c * d"
tac_generator = TACGenerator()
tac_generator.generate_tac(expr)
tac_generator.print_tac()
