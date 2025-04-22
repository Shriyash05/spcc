class CodeGenerator:
    def __init__(self):
        self.temp_count = 1
        self.reg_count = 0

    def generate_code(self, tac):
        for instruction in tac:
            self.process_instruction(instruction)

    def process_instruction(self, instruction):
        result, expression = instruction.split(' = ')
        result = result.strip()
        expression = expression.strip()

        # Handle simple operators
        if '+' in expression:
            op1, op2 = expression.split('+')
            print(f"ADD R{self.reg_count}, {op1.strip()}, {op2.strip()}")
        elif '-' in expression:
            op1, op2 = expression.split('-')
            print(f"SUB R{self.reg_count}, {op1.strip()}, {op2.strip()}")
        elif '*' in expression:
            op1, op2 = expression.split('*')
            print(f"MUL R{self.reg_count}, {op1.strip()}, {op2.strip()}")
        elif '/' in expression:
            op1, op2 = expression.split('/')
            print(f"DIV R{self.reg_count}, {op1.strip()}, {op2.strip()}")
        else:
            print(f"MOV R{self.reg_count}, {expression.strip()}")
        
        self.reg_count += 1

# Example Three Address Code (TAC)
tac_code = [
    "t1 = a + b",
    "t2 = t1 * c",
    "t3 = t2 - d",
    "t4 = t3 / e",
    "t5 = t4 + f"
]

# Generate and print assembly-like code
code_gen = CodeGenerator()
code_gen.generate_code(tac_code)
