"""
Module for exploring the FSM and recording its shape.
"""

from collections import defaultdict, deque
from typing import Sequence

from common import Action, State


class StopExploration(Exception):
    """Raised when the FSM is fully explored"""


class Explorer:
    """
    Class for exploring the FSM and recording its shape.
    """

    # transitions (as discovered so far)
    transitions: dict[State, dict[Action, State]]

    # set of fully explored states
    explored: set[State]

    def __init__(self) -> None:
        self.explored = set()
        self.transitions = defaultdict(dict)

    def act(self, node: State) -> tuple[Sequence[Action], bool]:
        """
        Return a series of actions to take from the given node and whether
        it's exploration.
        """

        # First, see if we can explore from this node
        action = self.explore(node)
        if action is not None:
            return (action,), True

        # Otherwise, go to an unexplored node
        return self.find_unexplored(node), False

    def add_known_info(self) -> None:
        """
        Add information from the spec about the Z node.

        This is optional - it would also be discovered.

        In a real system, this would be read from configuration rather than
        hard-coded here.
        """
        self.add_transition("Z", "-", "A")

    def add_transition(self, node: State, action: Action, successor: State) -> None:
        """
        Add information about a just-explored transition.
        """

        self.transitions[node][action] = successor

        if len(self.transitions[node]) == len(self.valid_actions(node)):
            self.explored.add(node)

    @staticmethod
    def valid_actions(node: State) -> set[Action]:
        """
        The valid actions from a node.

        This is "1", "2", "3" for all states except the terminal state Z,
        which only has the implicit transition to A (represented as "-").

        In a real system, this would be read from configuration rather than
        hard-coded here.
        """

        return {"-"} if node == "Z" else {"1", "2", "3"}

    def explore(self, node: State) -> Action | None:
        """
        Choose a direction to explore from the given node, or None if the
        node has no remaining unexplored actions, and whether this
        completes the exploration from this node.

        Since the actions are all undistinguished and there's no concern
        about bias, we arbitrarily choose the first unexplored action.
        """
        candidates = self.valid_actions(node) - self.transitions[node].keys()
        return min(candidates) if candidates else None

    def find_unexplored(self, node: State) -> Sequence[Action]:
        """
        Find an unexplored node starting from the given node.

        Since all the transitions are deterministic and equal cost (except
        perhaps the implicit Z->A transition), we can use a uniform-cost
        search with a plain queue, a breadth-first search.
        """
        seen = set()
        frontier: deque[tuple[tuple[Action, ...], State]] = deque()
        path: tuple[Action, ...] = ()
        while node in self.explored:
            seen.add(node)

            for action, successor in self.transitions[node].items():
                if successor not in seen:
                    frontier.append((path + (action,), successor))

            try:
                path, node = frontier.popleft()
            except IndexError as exc:
                raise StopExploration from exc

        return path
