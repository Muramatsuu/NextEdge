# test_nextedge.py
"""
Tests for NextEdge module.
"""

import unittest
from nextedge import NextEdge

class TestNextEdge(unittest.TestCase):
    """Test cases for NextEdge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NextEdge()
        self.assertIsInstance(instance, NextEdge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NextEdge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
