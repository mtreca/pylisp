from typing import List


class LispObject:
    def __init__(self, val):
        self.val = val


class LispInteger(LispObject):
    def __repr__(self) -> str:
        return str(self.val)


class LispSymbol(LispObject):
    def __repr__(self) -> str:
        return self.val


class LispList(LispObject):
    def __repr__(self) -> str:
        return "(" + " ".join([atom.__repr__() for atom in self.val]) + ")"

    def __iter__(self):
        for atom in self.val:
            yield atom


def atom_to_object(atom: str) -> LispObject:
    match atom:
        case x if is_integer(x):
            return LispInteger(int(x))
        case _:
            return LispSymbol(x)


def list_to_object(atoms: List[LispObject]) -> LispList:
    return LispList(atoms)


def object_to_string(object: LispObject) -> str:
    return object.__repr__()


def is_integer(x: str) -> bool:
    match x:
        case ["+" | "-", *_]:
            return is_integer(x[1:])
        case _:
            return x.isdigit()
