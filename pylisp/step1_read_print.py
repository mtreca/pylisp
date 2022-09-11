from typing import List

from lisp_printer import pr_str
from lisp_reader import read_str
from lisp_types import LispObject


def READ(x: str) -> LispObject:
    return read_str(x)


def EVAL(x: LispObject) -> LispObject:
    return x


def PRINT(x: LispObject) -> str:
    y = pr_str(x)
    print(y)
    return y


def REP(x: str) -> str:
    return PRINT(EVAL(READ(x)))


def main() -> None:
    while True:
        match input("user> "):
            case "exit":
                exit()
            case x:
                REP(x)


if __name__ == "__main__":
    main()
