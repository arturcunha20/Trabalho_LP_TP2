# logic_eval

def xor(a, b):
    return (a or b) and not (a and b)


class LogicEval:
    symbols = {}

    # Design Pattern: Dispatch Table
    operators = {
        "or": lambda args: args[0] or args[1],
        "not": lambda args: not args[0],
        "xor": lambda args: xor(args[0], args[1]),
        "and": lambda args: args[0] and args[1],
        "+": lambda args: args[0] + args[1],
        "-": lambda args: args[0] - args[1],
        "*": lambda args: args[0] * args[1],
        "/": lambda args: args[0] / args[1],
        "attrib": lambda args: LogicEval._attrib(args),
        "print": lambda args: print(*args),
        "for": lambda args: LogicEval._for(args)
    }

    @staticmethod
    def _for(args):
        var, low, hi, code = args
        if type(low) is not float or type(hi) is not float:
            raise Exception("For range can't use booleans")
        iterator = low
        while iterator <= hi:
            LogicEval.symbols[var] = iterator
            LogicEval.evaluate(code)
            iterator += 1
        return None

    @staticmethod
    def _attrib(args):
        value = args[1]
        LogicEval.symbols[args[0]] = value
        ### LogicEval.symbols[args[0]] = { "value": value, "type": ... }
        # print(LogicEval.symbols)
        return None

    @staticmethod
    def evaluate(ast):
        if type(ast) in (bool, float):
            return ast
        if type(ast) is dict:
            return LogicEval._eval_operator(ast)
        if type(ast) is str:
            var = ast
            if var in LogicEval.symbols:
                return LogicEval.symbols[ast]
            raise Exception(f"Undefined variable: {var}")
        if type(ast) is list:
            ans = None
            for a in ast:
                ans = LogicEval.evaluate(a)
            return ans

        raise Exception("Unknown AST type")

    @staticmethod
    def _eval_operator(ast):

        if 'op' in ast:
            op = ast["op"]
            # [ {str : "batatas"}, 10 ]
            args = [LogicEval.evaluate(a) for a in ast['args']]
            # [ "batatas", 10 ]
            if "code" in ast:
                args.append(ast["code"])
            if op in LogicEval.operators:
                func = LogicEval.operators[op]
                return func(args)
            else:
                raise Exception(f"Unknown operator {op}")

        if 'var' in ast:
            return ast['var']

        if 'str' in ast:
            return ast['str']
