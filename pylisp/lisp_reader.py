import re
from collections import deque
from typing import Deque, List

from lisp_types import LispObject, LispList, atom_to_object, list_to_object


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


def read_str(string: str) -> LispObject:
    tokens = tokenize(string)
    reader = Reader(tokens)
    return read_form(reader)


def read_form(reader: Reader) -> LispObject:
    match reader.peek():
        case ")":
            raise Exception("Unexpected ')'")
        case "(":
            return read_list(reader)
        case _:
            return read_atom(reader)


def read_list(reader: Reader) -> LispList:
    atoms = []
    _ = reader.next()

    while (out := reader.peek()) != ")":
        if out is None:
            raise Exception("Unbalanced parenthesis in expression")
        atoms.append(read_form(reader))

    _ = reader.next()

    return list_to_object(atoms)


def read_atom(reader: Reader) -> LispObject:
    return atom_to_object(reader.next())
