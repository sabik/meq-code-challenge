"""Module to visualise the FSM"""

import subprocess
from typing import Iterable

from common import Action, State


def render_fsm(transitions: dict[State, dict[Action, State]]) -> Iterable[str]:
    """Render the FSM to graphviz "dot" language"""

    yield "digraph fsm {"

    for node in sorted(transitions):
        for action, successor in transitions[node].items():
            if action == "-":
                attr = "[weight=0]"
            else:
                attr = f'[label="{action}"]'

            yield f"  {node} -> {successor} {attr}"

    yield "}"


def run_dot(fname_base: str) -> None:
    """Run the graphviz `dot` command to convert .dot to .png"""

    subprocess.run(
        ["dot", "-Tpng", "-o", f"{fname_base}.png", f"{fname_base}.dot"],
        check=True,
    )
