# test_nodequantum.py
"""
Tests for nodeQuantum module.
"""

import unittest
from nodequantum import nodeQuantum

class TestnodeQuantum(unittest.TestCase):
    """Test cases for nodeQuantum class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = nodeQuantum()
        self.assertIsInstance(instance, nodeQuantum)
        
    def test_run_method(self):
        """Test the run method."""
        instance = nodeQuantum()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
