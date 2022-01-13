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

    @staticmethod
    def loadTable(args):
        nomeTable = args['var']['var']
        nomeFicheiro = args['var']['fim']['var']['str']

        if nomeTable not in LogicEval.BaseDeDados:
            LogicEval.BaseDeDados[nomeTable] = pd.read_csv(nomeFicheiro)
            float_transform(nomeTable)
        else:
            return "Tabela ja existe"

        return "LOAD " + nomeTable

    @staticmethod
    def showTable(args):
        nomeTable = args['var']['var']

        if nomeTable in LogicEval.BaseDeDados:
            print(LogicEval.BaseDeDados[nomeTable])
        else:
            print("Tabela nao existe")

        return "SHOW " + nomeTable

    @staticmethod
    def savetabela(args):
        nomeTable = args['var']['var']
        nomeFicheiro = args['var']['fim']['var']['str']

        if nomeTable in LogicEval.BaseDeDados:
            pd.DataFrame(LogicEval.BaseDeDados[nomeTable]).to_csv(nomeFicheiro, index=False)
        else:
            print("Table nao existe")

        return "SAVE " + nomeTable

    @staticmethod
    def discardTable(args):
        nomeTable = args['var']['var']

        if nomeTable in LogicEval.BaseDeDados:
            LogicEval.BaseDeDados.pop(nomeTable)
        else:
           print("Tabela nao existe")
        return "DISCARD " + nomeTable

    @staticmethod
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
                    info = 0
                    Table, info = tableWhereOperacoes(nomeTable,op,var,args,campo,campos)
                    if info != 1:
                        print(Table)
                    tableFinal = Table
                    existe_limit = 0
                    hehe = verificarANDWhere(args)
                    if hehe == True:
                        esp = args['var']['args']['fim']['args']['args']
                        ola = verificarAND(esp)
                        tableFinal = tableAndOperacoes(esp,tableFinal)
                        if esp['args']['args'] == ';':
                            print("ACABOU")
                        else:
                            while (ola == True):
                                if esp['args']['args']['args'] == "LIMIT":
                                    limit_print_and(tableFinal,esp['args']['args']['var']['nr'])
                                    existe_limit = 1
                                    break

                                joj = verificarANDESP(esp)
                                if joj == True:
                                    esp = esp['args']['args']
                                    if esp['args']['args'] == ';':
                                        tableFinal = tableAndOperacoes(esp,tableFinal)
                                        break
                                    else:
                                        tableFinal = tableAndOperacoes(esp,tableFinal)
                        if existe_limit == 0:
                            tableFinal = print_limit(campos,tableFinal)
                            print(tableFinal)
        else:
           print("Tabela nao existe")


def tableAndOperacoes(args,table):
    op = args['args']['op']
    var = args['args']['var']
    campo = args['args']['campo']

    #print("----> ",op , " | ", var, " | ", campo)

    if op == '=':
        if 'str' in var:
            isTRUE = table[campo] == var['str']
            aa = table[isTRUE]
            return aa
        if 'nr' in var:
            isTRUE = table[campo] == var['nr']
            aa = table[isTRUE]
            return aa

    if op == ">":
        isTRUE = table[campo] > var['nr']
        aa = table[isTRUE]
        return aa

    if op == "<":
        isTRUE = table[campo] < var['nr']
        aa = table[isTRUE]
        return aa

    if op == ['<', '>']:
        if 'str' in var:
            isTRUE = table[campo] != var['str']
            aa = table[isTRUE]
            return aa
        if 'nr' in var:
            isTRUE = table[campo] != var['nr']
            aa = table[isTRUE]
            return aa

    if op == ['<', '=']:
        isTRUE = table[campo] <= var['nr']
        aa = table[isTRUE]
        return aa

    if op == ['>', '=']:
        isTRUE = table[campo] >= var['nr']
        aa = table[isTRUE]
        return aa

def tableWhereOperacoes(nomeTable,op,var,args,campo,campos):
    if op == "=":
        if 'str' in var:
            isTRUE = LogicEval.BaseDeDados[nomeTable][campo] == var['str']
            aa = LogicEval.BaseDeDados[nomeTable][isTRUE]
            bb = args['var']['args']['fim']
            table,info = returnTable(bb, campos, aa)

            return table,info

        if 'nr' in var:
            isTRUE = LogicEval.BaseDeDados[nomeTable][campo] == var['nr']
            aa = LogicEval.BaseDeDados[nomeTable][isTRUE]
            bb = args['var']['args']['fim']
            table,info = returnTable(bb, campos, aa)
            return table,info

    if op == ">":
        isTRUE = LogicEval.BaseDeDados[nomeTable][campo] > var['nr']
        aa = LogicEval.BaseDeDados[nomeTable][isTRUE]
        bb = args['var']['args']['fim']
        table, info = returnTable(bb, campos, aa)
        return table, info

    if op == "<":
        isTRUE = LogicEval.BaseDeDados[nomeTable][campo] < var['nr']
        aa = LogicEval.BaseDeDados[nomeTable][isTRUE]
        bb = args['var']['args']['fim']
        table, info = returnTable(bb, campos, aa)
        return table, info

    if op == ['<', '>']:
        if 'str' in var:
            isTRUE = LogicEval.BaseDeDados[nomeTable][campo] != var['str']
            aa = LogicEval.BaseDeDados[nomeTable][isTRUE]
            bb = args['var']['args']['fim']
            table,info = returnTable(bb, campos, aa)
            return table,info

        if 'nr' in var:
            isTRUE = LogicEval.BaseDeDados[nomeTable][campo] != var['nr']
            aa = LogicEval.BaseDeDados[nomeTable][isTRUE]
            bb = args['var']['args']['fim']
            table,info = returnTable(bb, campos, aa)
            return table,info

    if op == ['<', '=']:
        isTRUE = LogicEval.BaseDeDados[nomeTable][campo] <= var['nr']
        aa = LogicEval.BaseDeDados[nomeTable][isTRUE]
        bb = args['var']['args']['fim']
        table, info = returnTable(bb, campos, aa)
        return table, info

    if op == ['>', '=']:
        isTRUE = LogicEval.BaseDeDados[nomeTable][campo] >= var['nr']
        aa = LogicEval.BaseDeDados[nomeTable][isTRUE]
        bb = args['var']['args']['fim']
        table, info = returnTable(bb, campos, aa)
        return table, info

def verificarANDESP(args):
    if args['args']['args']['op'] == "AND":
        return True
    else:
        return False

def verificarANDWhere(args):
    if args['var']['args']['fim']['args']['args']['op'] == "AND":
        return True

def verificarAND(args):
    if args['op'] == "AND":
        return True
    else:
        return False

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

def returntablewhere(campos,table):
    if campos == '*':
        return table
    else:
        return table[campos]

def returnTable(bb,campos,aa):
    table = returntablewhere(campos, aa)
    if bb['args']['args'] == ";":
        return table,0
    else:
        info = limit(aa, campos, bb)
        return aa,1

def limit(table,campos,bb):
    if verificarLIMITWHERE(bb) == True:
        info = 1
        table = print_limit(campos, table)
        ff = pd.DataFrame(table)
        print(ff.head(int(bb['args']['args']['var']['nr'])))
        return info

def limit_print_and(table,num):
    ff = pd.DataFrame(table)
    print(ff.head(int(num)))