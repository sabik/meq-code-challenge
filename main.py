"""
Main program (controller)
"""

import os

from client import Client
from explorer import Explorer, StopExploration
from visualise import render_fsm, run_dot


def do_explore(c: Client, e: Explorer) -> None:
    """
    Run the exploration of the FSM
    """
    e.add_known_info()

    node = c.recv_state()

    try:
        while True:
            actions, exploring = e.act(node)
            for action in actions:
                c.send_action(action)
                successor = c.recv_state()
                if exploring:
                    e.add_transition(node, action, successor)
                node = successor
    except StopExploration:
        pass


def main() -> None:
    """
    Main program - run the exploration then output it
    """

    host = os.environ["HOST"]
    port = int(os.environ["PORT"])
    fname_base = os.environ["FNAME_BASE"]

    e = Explorer()
    with Client(host, port) as c:
        do_explore(c, e)

    with open(f"{fname_base}.dot", "w", encoding="ascii") as fh:
        fh.writelines(line + "\n" for line in render_fsm(e.transitions))

    run_dot(fname_base)


if __name__ == "__main__":
    main()
