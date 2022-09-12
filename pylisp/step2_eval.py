import functools
from typing import Dict

from lisp_printer import pr_str
from lisp_reader import read_str
from lisp_types import LispList, LispObject, LispSymbol

REPL_ENV = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: int(a / b),
}


def eval_ast(ast: LispObject, env: Dict) -> LispObject:
    if isinstance(ast, LispList):
        return [EVAL(x, env) for x in ast]
    elif isinstance(ast, LispSymbol):
        return env[ast.val]
    else:
        return ast


def READ(str: str) -> LispObject:
    return read_str(str)


def EVAL(ast: LispObject, env: Dict) -> LispObject:
    if isinstance(ast, LispList):
        if ast.val is []:
            return ast
        else:
            fn, *args = eval_ast(ast, env)
            return functools.reduce(fn, [arg.val for arg in args])
    else:
        return eval_ast(ast, env)


def PRINT(exp: LispObject) -> str:
    str = pr_str(exp)
    print(str)
    return str


def REP(str: str) -> str:
    return PRINT(EVAL(READ(str), REPL_ENV))


def main() -> None:
    while True:
        match input("user> "):
            case "exit":
                exit()
            case x:
                REP(x)


if __name__ == "__main__":
    main()
