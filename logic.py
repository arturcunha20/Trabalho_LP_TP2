# logic.py
from logic_grammar import LogicGrammar
from pprint import PrettyPrinter
import sys

pp = PrettyPrinter()
lg = LogicGrammar()
lg.build()

with open("t.txt", "r") as file:
    contents = file.read()
    try:
        ans = lg.parse(contents)
        pp.pprint(ans)
    except Exception as e:
        print(f'\033[91m-> {e}\033[0m')

if len(sys.argv) == 2:
    with open(sys.argv[1], "r") as file:
        contents = file.read()

else:
    for expr in iter(lambda: input(">> "), ""):
        try:
            ans = lg.parse(expr)
            pp.pprint(ans)
        except Exception as e:
            print(f'\033[91m-> {e}\033[0m')