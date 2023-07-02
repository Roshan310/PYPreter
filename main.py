import sys
INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'

class Token():

    def __init__(self, type, value) -> None:
        self.type = type
        self.value = value


    def __str__(self) -> str:
        return f"Token({self.type}, {self.value})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
class Interpreter():

    def __init__(self, text) -> None:
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception("Error parsing input!! ")
    
    def get_next_token(self):

        text = self.text
        if self.pos > len(text) - 1:
            return Token(EOF, None)
        
        current_char = text[self.pos]

        if current_char.isdigit():
            self.pos += 1
            return Token(INTEGER, int(current_char))
        
        if current_char == '+':
            self.pos += 1
            return Token(PLUS, current_char)

        self.error()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()

        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token
        self.eat(PLUS)

        right = self.current_token
        self.eat(INTEGER)

        result = left.value + right.value
        return result
    

def main():
    while True:
        text = input("Calc> ")
        if text == 'exit':
            sys.exit()
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

main()