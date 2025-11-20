"""Tests for the explorer module"""

import unittest

from explorer import Explorer  # pylint: disable=wildcard-import,unused-wildcard-import
from visualise import *  # pylint: disable=wildcard-import,unused-wildcard-import


class TestVisualise(unittest.TestCase):
    """Tests for the Explorer class"""

    def setUp(self) -> None:
        """Test setup"""
        e = Explorer()

        e.add_known_info()

        e.add_transition("A", "1", "B")
        e.add_transition("A", "2", "C")
        e.add_transition("A", "3", "C")

        e.add_transition("B", "1", "C")
        e.add_transition("B", "3", "Z")

        self.transitions = e.transitions

    def test_visualise(self) -> None:
        """Test the Explorer.explore() method"""
        self.assertEqual(
            list(render_fsm(self.transitions)),
            [
                "digraph fsm {",
                '  A -> B [label="1"]',
                '  A -> C [label="2"]',
                '  A -> C [label="3"]',
                '  B -> C [label="1"]',
                '  B -> Z [label="3"]',
                "  Z -> A [weight=0]",
                "}",
            ],
        )
