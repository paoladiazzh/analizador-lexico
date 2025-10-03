import sys

class Parser:
    def __init__(self, text):
        self.program_input = text
        self.input_index = 0
        self.word = ""
        self.get_next_word()

    def get_next_word(self):
        # Skip whitespace
        while self.input_index < len(self.program_input) and self.program_input[self.input_index].isspace():
            self.input_index += 1

        if self.input_index == len(self.program_input):
            self.word = "eof"
            return "eof"

        # operadores
        operators = ['+', '-', '*', '/', '(', ')', ',', '[', ']']
        for op in operators:
            if self.program_input.startswith(op, self.input_index):
                self.word = op
                self.input_index += len(op)
                return self.word

        # numeros
        if self.program_input[self.input_index].isdigit():
            while self.input_index < len(self.program_input) and self.program_input[self.input_index].isdigit():
                self.input_index += 1
            self.word = "num"
            return "num"

        # id
        if self.program_input[self.input_index].isalpha():
            while self.input_index < len(self.program_input) and (self.program_input[self.input_index].isalnum() or self.program_input[self.input_index] == '_'):
                self.input_index += 1
            self.word = "id"
            return "id"

        # error
        self.word = "error"
        return "error"

    def parse(self):
        res = self.expr_list()
        if res and self.word == "eof":
            print("Parsing completed :) ")
        else:
            print("Syntax error :( ")

    # reglas de produccion
    def expr(self):
        res = self.term()
        if not res:
            return False
        return self.expr_pr()

    def expr_pr(self):
        if self.word in ['+', '-']:
            self.get_next_word()
            res = self.term()
            if not res:
                return False
            return self.expr_pr()
        elif self.word in ["eof", ")", ",", "]"]:
            return True
        else:
            return False

    def term(self):
        res = self.factor()
        if not res:
            return False
        return self.term_pr()

    def term_pr(self):
        if self.word in ['*', '/']:
            self.get_next_word()
            res = self.factor()
            if not res:
                return False
            return self.term_pr()
        elif self.word in ["eof", ")", "+", "-", ",", "]"]:
            return True
        else:
            return False

    def factor(self):
        if self.word == '(':
            self.get_next_word()
            res = self.expr()
            if not res:
                return False
            if self.word == ')':
                self.get_next_word()
                return self.factor_pr_after_paren()
            else:
                return False
        elif self.word == "id":
            self.get_next_word()
            return self.factor_pr_after_ident()
        elif self.word == "num":
            self.get_next_word()
            return self.factor_pr_after_num()
        else:
            return False

    def factor_pr_after_paren(self):
        if self.word == '[':
            self.get_next_word()
            res = self.expr()
            if not res:
                return False
            if self.word == ']':
                self.get_next_word()
                return True
            else:
                return False
        elif self.word == '(':
            self.get_next_word()
            res = self.expr_list()
            if not res:
                return False
            if self.word == ')':
                self.get_next_word()
                return True
            else:
                return False
        else:
            return True

    def factor_pr_after_ident(self):
        if self.word == '[':
            self.get_next_word()
            res = self.expr()
            if not res:
                return False
            if self.word == ']':
                self.get_next_word()
                return True
            else:
                return False
        elif self.word == '(':
            self.get_next_word()
            res = self.expr_list()
            if not res:
                return False
            if self.word == ')':
                self.get_next_word()
                return True
            else:
                return False
        else:
            return True

    def factor_pr_after_num(self):
        return True

    def expr_list(self):
        res = self.expr()
        if not res:
            return False
        return self.expr_list_pr()

    def expr_list_pr(self):
        if self.word == ',':
            self.get_next_word()
            res = self.expr()
            if not res:
                return False
            return self.expr_list_pr()
        elif self.word in [")", "eof", "]"]:
            return True
        else:
            return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python parser.py archivo.txt")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, "r") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {filename}")
        sys.exit(1)

    parser = Parser(text)
    parser.parse()
