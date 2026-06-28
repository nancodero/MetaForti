# test_fortilink.py
"""
Tests for FortiLink module.
"""

import unittest
from fortilink import FortiLink

class TestFortiLink(unittest.TestCase):
    """Test cases for FortiLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FortiLink()
        self.assertIsInstance(instance, FortiLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FortiLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
