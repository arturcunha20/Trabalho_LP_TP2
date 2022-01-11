# logic_eval
from pprint import PrettyPrinter
import pandas as pd

pp = PrettyPrinter()

class LogicEval:
    symbols = {}
    BaseDeDados = {}

    # Design Pattern: Dispatch Table
    operators = {
        'SAVE': lambda args: LogicEval.savetabela(args),
        'DISCARD': lambda args: LogicEval.discardTable(args),
        'LOAD': lambda args: LogicEval.loadTable(args),
        'SHOW': lambda args: LogicEval.showTable(args),
        'SELECT': lambda args: LogicEval.selectTable(args),
    }
    @staticmethod
    def evaluate(args):
        if type(args) is list:
            ans = None
            for a in args:
                ans = LogicEval.evaluate(a)
                return ans

        if args['args'] in LogicEval.operators:
            f = LogicEval.operators[args['args']]
            return f(args)


    def loadTable(args):
        nomeTable = args['var']['var']
        nomeFicheiro = args['var']['fim']['var']['str']

        if nomeTable not in LogicEval.BaseDeDados:
            LogicEval.BaseDeDados[nomeTable] = pd.read_csv(nomeFicheiro)
            float_transform(nomeTable)
        else:
            return "Tabela ja existe"

        return "LOAD " + nomeTable

    def showTable(args):
        nomeTable = args['var']['var']
        if nomeTable in LogicEval.BaseDeDados:
            print(LogicEval.BaseDeDados[nomeTable])
        else:
            print("Tabela nao existe")

        return "SHOW " + nomeTable

    def savetabela(args):
        nomeTable = args['var']['var']
        nomeFicheiro = args['var']['fim']['var']['str']

        if nomeTable in LogicEval.BaseDeDados:
            pd.DataFrame(LogicEval.BaseDeDados[nomeTable]).to_csv(nomeFicheiro, index=False)
        else:
            print("Table nao existe")

        return "SAVE " + nomeTable

    def discardTable(args):
        nomeTable = args['var']['var']

        if nomeTable in LogicEval.BaseDeDados:
            LogicEval.BaseDeDados.pop(nomeTable)
        else:
           print("Tabela nao existe")
        return "DISCARD " + nomeTable

    def selectTable(args):
        campos = args['var']['var']
        nomeTable = args['var']['args']['var']
        if nomeTable in LogicEval.BaseDeDados:
            if args['var']['args']['fim'] == ';':
                select_prints(campos, nomeTable)
            else:
                if verificarLIMIT(args) == True:
                    table = print_limit(campos,LogicEval.BaseDeDados[nomeTable])
                    ff = pd.DataFrame(table)
                    print(ff.head(int(args['var']['args']['fim']['var']['nr'])))

                if args['var']['args']['fim']['var'] == 'WHERE':
                    op = args['var']['args']['fim']['args']['op']
                    campo = args['var']['args']['fim']['args']['campo']
                    var = args['var']['args']['fim']['args']['var']

                    if op == "=":
                        if 'str' in var:
                            isTRUE = LogicEval.BaseDeDados[nomeTable][campo] == var['str']
                            aa = LogicEval.BaseDeDados[nomeTable][isTRUE]
                            bb = args['var']['args']['fim']
                            limit_where_prints(bb, campos, aa)

                        if 'nr' in var:
                            isTRUE = LogicEval.BaseDeDados[nomeTable][campo] == var['nr']
                            aa = LogicEval.BaseDeDados[nomeTable][isTRUE]
                            bb = args['var']['args']['fim']
                            limit_where_prints(bb, campos, aa)

                    if op == ">":
                        isTRUE = LogicEval.BaseDeDados[nomeTable][campo] > var['nr']
                        aa = LogicEval.BaseDeDados[nomeTable][isTRUE]
                        bb = args['var']['args']['fim']
                        limit_where_prints(bb, campos, aa)

                    if op == "<":
                        isTRUE = LogicEval.BaseDeDados[nomeTable][campo] < var['nr']
                        aa = LogicEval.BaseDeDados[nomeTable][isTRUE]
                        bb = args['var']['args']['fim']
                        limit_where_prints(bb, campos, aa)

                    if op == ['<','>']:
                        if 'str' in var:
                            isTRUE = LogicEval.BaseDeDados[nomeTable][campo] != var['str']
                            aa = LogicEval.BaseDeDados[nomeTable][isTRUE]
                            bb = args['var']['args']['fim']
                            limit_where_prints(bb, campos, aa)
                        if 'nr' in var:
                            isTRUE = LogicEval.BaseDeDados[nomeTable][campo] != var['nr']
                            print(isTRUE)
                            aa = LogicEval.BaseDeDados[nomeTable][isTRUE]
                            bb = args['var']['args']['fim']
                            limit_where_prints(bb, campos, aa)

                    if op == ['<','=']:
                        isTRUE = LogicEval.BaseDeDados[nomeTable][campo] <= var['nr']
                        aa = LogicEval.BaseDeDados[nomeTable][isTRUE]
                        bb = args['var']['args']['fim']
                        limit_where_prints(bb, campos, aa)

                    if op == ['>','=']:
                        isTRUE = LogicEval.BaseDeDados[nomeTable][campo] >= var['nr']
                        aa = LogicEval.BaseDeDados[nomeTable][isTRUE]
                        bb = args['var']['args']['fim']
                        limit_where_prints(bb, campos, aa)
        else:
           print("Tabela nao existe")


def verificarLIMITWHERE(args):
    if args['args']['args']['args'] == "LIMIT":
        return True

def verificarLIMIT(args):
    if args['var']['args']['fim']['args'] == "LIMIT":
        return True
    else:
        return False


def select_prints(campos, nomeTable):
    tabela = pd.DataFrame(LogicEval.BaseDeDados[nomeTable])
    if campos == '*':
        print(LogicEval.BaseDeDados[nomeTable])
    else:
        print(tabela[campos])

def select_prints_where(campos,table):
    if campos == '*':
        print(table)
        print(" ")
    else:
        print(table[campos])
        print(" ")

def print_limit(campos,table):
    if campos == '*':
        return (table)
    else:
        return (table[campos])

def float_transform(nomeTable):
    for x in LogicEval.BaseDeDados[nomeTable]:
        for j in LogicEval.BaseDeDados[nomeTable][x]:
            check_int = isinstance(j, float)
            if check_int == True:
                j = float(j)

def limit_where_prints(bb,campos,aa):
    if bb['args']['args'] == ";":
        select_prints_where(campos, aa)
    elif verificarLIMITWHERE(bb) == True:
        table = print_limit(campos, aa)
        ff = pd.DataFrame(table)
        print(ff.head(int(bb['args']['args']['var']['nr'])))