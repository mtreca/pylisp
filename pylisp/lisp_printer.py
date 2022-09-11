from lisp_types import LispObject, object_to_string

from typing import List


def pr_str(atoms: LispObject) -> str:
    return object_to_string(atoms)
