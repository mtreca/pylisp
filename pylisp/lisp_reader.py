import re
from collections import deque
from typing import Deque, List

from lisp_types import atom_to_object, LispItem, LispAtom, LispList


class Reader:
    def __init__(self, tokens: List[str]):
        self.tokens: Deque = deque(tokens)

    def peek(self) -> str:
        return self.tokens[0] if len(self.tokens) > 0 else None

    def next(self) -> str:
        return self.tokens.popleft()


def tokenize(string: str) -> List[str]:
    match = r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"?|;.*|[^\s\[\]{}('"`,;)]*)"""
    tokenizer = re.compile(match)
    return tokenizer.findall(string)


def read_str(string: str) -> LispItem:
    tokens = tokenize(string)
    reader = Reader(tokens)
    return read_form(reader)


def read_form(reader: Reader) -> LispItem:

    if (next := reader.peek()) == ")":
        raise Exception("Unexpected ')'")
    elif next == "(":
        return read_list(reader)
    else:
        return read_atom(reader)


def read_list(reader: Reader) -> LispList:
    atoms = []
    _ = reader.next()

    while (out := reader.peek()) != ")":
        if out is None:
            raise Exception("Unbalanced parenthesis in expression")
        atoms.append(read_form(reader))

    _ = reader.next()

    return atoms


def read_atom(reader: Reader) -> LispAtom:
    return atom_to_object(reader.next())
