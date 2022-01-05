# logic_eval
import csv
from pprint import PrettyPrinter

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
        'SHOW': lambda args: LogicEval.showTable(args)
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
            LogicEval.a_csv_file = open(nomeFicheiro, "r")
            LogicEval.BaseDeDados[nomeTable] = csv.DictReader(LogicEval.a_csv_file)

        else:
            return "Tabela ja existe"

    def showTable(args):
        nomeTable = args['var']['var']

        if nomeTable in LogicEval.BaseDeDados:
            for x in LogicEval.BaseDeDados[nomeTable]:
                print(x)

            LogicEval.a_csv_file.seek(0)
            next(LogicEval.a_csv_file)
        else:
            return "Tabela nao existe"

        return "SHOW " + nomeTable


    def savetabela(args):
        for x in LogicEval.BaseDeDados['produtos']:
            print(x)

        return "SAVE"

    def discardTable(args):
        return "DISCARD"

