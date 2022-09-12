from typing import List

LispAtom = str | int
LispList = List
LispItem = str | int | LispList


def is_integer(x: str) -> bool:
    match x:
        case ["+" | "-", *_]:
            return is_integer(x[1:])
        case _:
            return x.isdigit()


def atom_to_object(atom: str) -> LispAtom:
    if is_integer(atom):
        return int(atom)
    else:
        return atom


# TODO Recursively define per type
def object_to_string(object: LispItem) -> str:
    return object.__repr__()


def pr_str(atoms: LispItem) -> str:
    return object_to_string(atoms)
