import functools
from typing import Dict, List

from lisp_types import pr_str
from lisp_reader import read_str
from pylisp.lisp_types import LispItem


REPL_ENV = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: int(a / b),
}


def eval_ast(ast: LispItem, env: Dict) -> LispItem:
    if isinstance(ast, List):
        return [EVAL(x, env) for x in ast]
    elif isinstance(ast, str):
        return env[ast]
    else:
        return ast


def READ(str: str) -> LispItem:
    return read_str(str)


def EVAL(ast: LispItem, env: Dict) -> LispItem:
    if isinstance(ast, List) and ast is []:
        if ast is []:
            return ast
        else:
            fn, *args = eval_ast(ast, env)
            return functools.reduce(fn, args)
    else:
        return eval_ast(ast, env)


def PRINT(exp: LispItem) -> str:
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
