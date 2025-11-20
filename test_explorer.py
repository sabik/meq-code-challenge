"""Tests for the explorer module"""

import unittest

from explorer import *  # pylint: disable=wildcard-import,unused-wildcard-import


class TestExplorer(unittest.TestCase):
    """Tests for the Explorer class"""

    def setUp(self) -> None:
        """Test setup"""
        self.e = Explorer()

        self.e.add_known_info()

        self.e.add_transition("A", "1", "B")
        self.e.add_transition("A", "2", "C")
        self.e.add_transition("A", "3", "C")

        self.e.add_transition("B", "1", "C")
        self.e.add_transition("B", "3", "Z")

    def test_explore(self) -> None:
        """Test the Explorer.explore() method"""
        self.assertEqual(self.e.explore("A"), None)
        self.assertEqual(self.e.explore("B"), "2")
        self.assertEqual(self.e.explore("C"), "1")
        self.assertEqual(self.e.explore("Z"), None)

    def test_find_unexplored(self) -> None:
        """Test the Explorer.find_unexplored() method"""

        # A is fully explored, return path to B or C
        self.assertEqual(self.e.find_unexplored("A"), ("1",))

        # B and C are not fully explored, nothing to do
        self.assertEqual(self.e.find_unexplored("B"), ())
        self.assertEqual(self.e.find_unexplored("C"), ())

        # from Z, take the implicit transition then proceed as for A
        self.assertEqual(self.e.find_unexplored("Z"), ("-", "1"))

    def test_valid_actions(self) -> None:
        """Test the Explorer.valid_actions() method"""

        # test a few ordinary nodes
        self.assertEqual(self.e.valid_actions("A"), {"1", "2", "3"})
        self.assertEqual(self.e.valid_actions("K"), {"1", "2", "3"})
        self.assertEqual(self.e.valid_actions("Y"), {"1", "2", "3"})

        # test the terminal node
        self.assertEqual(self.e.valid_actions("Z"), {"-"})
