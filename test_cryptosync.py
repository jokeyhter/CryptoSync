# test_cryptosync.py
"""
Tests for CryptoSync module.
"""

import unittest
from cryptosync import CryptoSync

class TestCryptoSync(unittest.TestCase):
    """Test cases for CryptoSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoSync()
        self.assertIsInstance(instance, CryptoSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
