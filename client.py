"""
Communication with the server
"""

import logging
import socket
from typing import Any, Self, cast

from common import Action, State

logger = logging.getLogger(__name__)


class Client:
    """
    Communication with the server
    """

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __enter__(self) -> Self:
        self.s.connect((self.host, self.port))
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self.s.close()

    def recv_state(self) -> State:
        """Receive a state from the server"""
        while True:
            ch = self.s.recv(1)

            match ch:
                case b"\n":
                    pass
                case _ if b"A" <= ch <= b"Z":
                    return cast(State, ch.decode("ascii"))
                case _:
                    logger.warning("Received character %s from server", ch)

    def send_action(self, action: Action) -> None:
        """Send an action to the server"""
        if action != "-":
            self.s.sendall(action.encode("ascii") + b"\n")
