# logic_grammar.py
from logic_lexer import LogicLexer
import ply.yacc as pyacc

class LogicGrammar:
    def __init__(self):
        self.yacc = None
        self.lexer = None
        self.tokens = None

    def build(self, **kwargs):
        self.lexer = LogicLexer()
        self.lexer.build(**kwargs)
        self.tokens = self.lexer.tokens
        self.yacc = pyacc.yacc(module=self, **kwargs)

    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lexer)

    def p_varias00(self,p):
        """ vars : S"""
        p[0] = [p[1]]

    def p_varias01(self, p):
        """ vars : vars S"""
        p[0] = p[1]
        p[0].append(p[2])


    def p_S(self,p):
        """ S : comands
              | procedimentos
              | v
              | call_procedimentos"""
        p[0] = p[1]

    def p_comands(self,p):
        """ comands : DISCARD table
                    | LOAD table
                    | SAVE table
                    | SHOW table
                    | SELECT select
                    | CREATE table"""
        p[0] = {'var': p[2], 'args': p[1]}

    def p_table(self,p):
        """ table : TABLE var ';'
                  | TABLE var from
                  | TABLE var as """
        if len(p) == 4:
            p[0] = {'var': p[2], 'args': p[1], 'fim': p[3]}
        else:
            p[0] = p[1]

    def p_select(self,p):
        """ select : '*' from
                   | a_list from"""

        p[0] = {'var': p[1], 'args': p[2]}

    def p_aList00(self,p):
        """ a_list : var """
        p[0] = [p[1]]

    def p_aList01(self,p):
        """ a_list : a_list ',' var """
        p[0] = p[1]
        p[0].append(p[3])

    def p_as(self,p):
        """ as : AS string ';' """
        p[0] = {'var': p[2], 'args': p[1]}

    def p_var(self,p):
        """ v : var """
        p[0] = p[1]

    def p_from(self,p):
        """ from : FROM var ';'
                 | FROM var where
                 | FROM comands
                 | FROM var join
                 | FROM string ';' """

        if len(p) == 3:
            p[0] = {'var': p[2], 'args': p[1]}
        else:
            p[0] = {'var': p[2], 'args': p[1], 'fim': p[3]}

    def p_join(self,p):
        """ join : JOIN var using"""
        p[0] = {'var': p[2], 'args': [p[1],p[3]]}

    def p_using(self,p):
        """ using : USING '(' var '=' nr ')' ';'
                  | USING '(' var '=' string ')' ';' """
        p[0] = {'var': [p[3],p[5]], 'args': p[1], 'op': p[4], 'fim':p[7] , 'paren': [p[2],p[6]]}

    def p_where(self,p):
        """ where :  WHERE operadores """
        p[0] = {'var': p[1],'args': p[2]}

    def p_operadores00(self,p):
        """ operadores : var '=' nr rec
                       | var '=' string rec
                       | var '<' '>' nr rec
                       | var '<' '>' string rec
                       | var '<' nr rec
                       | var '>' nr rec
                       | var '<' '=' nr rec
                       | var '>' '=' nr rec"""

        if len(p)== 5:
            p[0] = {'var': [p[1], p[3]], 'op': p[2] , 'args': p[4]}
        elif len(p) == 6:
            p[0] = {'var': [p[1], p[4]], 'op': [p[2],p[3]], 'args': p[5]}

    def p_operadores01(self,p):
        """ rec : ';'
                | AND operadores
                | LIMIT nr ';' """

        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 3:
            p[0] = {'op': p[1], 'args': p[2]}
        elif len(p) == 4:
            p[0] = {'op': p[1], 'var': p[2] , 'fim':p[3]}

    def p_procedimentos00(self, p):
        """ procedimentos : PROCEDURE var DO list_com END """
        p[0] = {'var': p[2], 'list': p[4], 'args': [p[1], p[3], p[5]]}

    def p_procedimentos01(self, p):
        """ list_com : comands """
        p[0] = [p[1]]

    def p_procedimentos02(self,p):
        """ list_com : list_com comands """
        p[0] = p[1]
        p[0].append(p[2])

    def p_callProcedimentos(self,p):
        """ call_procedimentos : CALL var ';'"""
        p[0] = {'args': p[1], 'var': p[2] , "fim": p[3]}

    def p_error(self, p):
        if p:
            raise Exception(f"Syntax error: unexpected '{p.type}'")
        else:
            raise Exception("Syntax error: unexpected end of file")
