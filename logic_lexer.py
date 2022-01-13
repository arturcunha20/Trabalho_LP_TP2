# logic_lexer.py
import ply.lex as plex

class LogicLexer:
    tokens = ("var", "nr", "string", "LOAD", "TABLE", "FROM", "AS", "DISCARD", "SAVE", "SHOW", "SELECT", "WHERE", "AND", "LIMIT", "CREATE", "JOIN", "USING", "PROCEDURE", "DO", "END", "CALL")
    literals = ['(', ')', '=', '+', '-', '*', '/', '[', ']', '{', '}', ',', ';','<','>']
    t_ignore = " \n"

    def __init__(self):
        self.lexer = None

    def build(self, **kwargs):
            self.lexer = plex.lex(module=self, **kwargs)

    def input(self, string):
        self.lexer.input(string)

    def t_string(self, t):
        r'"[^"]*"'
        t.value = {"str": t.value[1:-1]}
        return t

    def t_str(self, t):
        r"TABLE|FROM|AS|DISCARD|LOAD|SAVE|SHOW|SELECT|WHERE|AND|LIMIT|CREATE|JOIN|USING|PROCEDURE|DO|END|CALL"
        t.type = t.value
        return t

    def t_var(self, t):
        r"[A-z_]+"
        return t

    def t_nr(self, t):
        r"[0-9]+(\.[0-9]+)?"
        t.value = {"nr": float(t.value)}
        return t

    def token(self):
        token = self.lexer.token()
        return token if token is None else token.type

    def t_error(self, t):
        print(f"Unexpected token: [{t.value[:10]}]")
        exit(1)

