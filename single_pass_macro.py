class MacroProcessor:
    def __init__(self):
        self.macros = {}

    def define_macro(self, macro_name, macro_body):
        """Defines a macro with its name and body."""
        self.macros[macro_name] = macro_body

    def process_line(self, line):
        """Processes each line and performs macro expansion."""
        words = line.split()

        # If the line is a macro definition
        if len(words) > 1 and words[0] == 'MACRO':
            macro_name = words[1]
            macro_body = []
            while True:
                body_line = input(f"Enter body for macro {macro_name}: ")
                if body_line == "END":
                    break
                macro_body.append(body_line)
            self.define_macro(macro_name, macro_body)
            print(f"Macro {macro_name} defined.")

        # If the line is a macro call
        elif words[0] in self.macros:
            macro_name = words[0]
            print("Expanding macro:", macro_name)
            self.expand_macro(macro_name)
        else:
            print("Processing line:", line.strip())

    def expand_macro(self, macro_name):
        """Expands the macro by replacing its call with its body."""
        macro_body = self.macros[macro_name]
        for line in macro_body:
            print(line)

    def process(self):
        """Main processing loop."""
        print("Start entering source code:")
        while True:
            line = input("Enter a line (or 'END' to stop): ")
            if line == "END":
                break
            self.process_line(line)


# Initialize the Macro Processor
processor = MacroProcessor()
processor.process()


# Enter a line (or 'END' to stop): MACRO ADD
# Enter body for macro ADD: MOV A, B
# Enter body for macro ADD: ADD A, C
# Enter body for macro ADD: END
# Macro ADD defined.

# Enter a line (or 'END' to stop): ADD
# Expanding macro: ADD
# MOV A, B
# ADD A, C
# Enter a line (or 'END' to stop): END
