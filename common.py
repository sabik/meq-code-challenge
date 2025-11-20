"""
Definitions of types and constants
"""

from typing import Literal

# Type for the actions, plus "-" to represent the implicit Z->A transition
type Action = Literal["1", "2", "3", "-"]

type State = Literal[
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
