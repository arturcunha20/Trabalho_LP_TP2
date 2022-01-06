# logic_eval
import csv
from pprint import PrettyPrinter
import pandas as pd

pp = PrettyPrinter()

class LogicEval:
    symbols = {}
    BaseDeDados = {}
    a_csv_file = None

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
            pd.DataFrame(LogicEval.BaseDeDados[nomeTable]).to_csv(nomeFicheiro,index=False)
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
        print("Entrou no select")